from stable_baselines import DQN, PPO2, A2C, ACKTR
from stable_baselines.common.env_checker import check_env
from stable_baselines.common.cmd_util import make_vec_env
from stable_baselines.deepq.policies import MlpPolicy
from stable_baselines.common.vec_env import DummyVecEnv

import signal
import time
import sys

import matplotlib.pyplot as plt
import numpy as np
import gym
import gym_skewb

def main():
    env = gym.make('Skewb-v0')
    check_env(env, warn=True)

    model = DQN(MlpPolicy, 
            env, 
            verbose=1,
            learning_rate=0.001,
            buffer_size=50000,
            exploration_fraction=0.3,
            exploration_final_eps=0.01,
            train_freq=4,
            learning_starts=10000,
            target_network_update_freq=1000,
            gamma=0.99,
            prioritized_replay=True,
            prioritized_replay_alpha=0.6
        ).learn(total_timesteps=2000000, log_interval=800)#,
            #callback=create_callback_func())

    print(model.learning_rate)

    print("Saving...")
    model.save("model.pkl")

def create_callback_func():
    n_steps = 0
    def callback_func(_locals, _globals):
        """
        Callback called at each step (for DQN an others) or after n steps (see ACER or PPO2)
        :param _locals: (dict)
        :param _globals: (dict)
        """
        nonlocal n_steps
        log_dir = "tmp/"
        # Retrieve the self object
        self_ = _locals['self']
        # Print stats every 1000 calls
        if (n_steps + 1) % 1000 == 0:
            print("test")
            # Evaluate policy training performance
            x, y = ts2xy(load_results(log_dir), 'timesteps')
            if len(x) > 0:
                mean_reward = np.mean(y[-100:])
                print(x[-1], 'timesteps')
                print("Best mean reward: {:.2f} - Last mean reward per episode: {:.2f}".format(self_.best_mean_reward, mean_reward))

                # New best model, you could save the agent here
                if mean_reward > self_.best_mean_reward:
                    self_.best_mean_reward = mean_reward
                    # Example for saving best model
                    print("Saving new best model")
                    self_.save(log_dir + 'best_model.pkl')
        n_steps += 1
        # Returning False will stop training early
        return True

def exit_gracefully(signum, frame):
    # restore the original signal handler as otherwise evil things will happen
    # in raw_input when CTRL+C is pressed, and our signal handler is not re-entrant
    signal.signal(signal.SIGINT, original_sigint)

    try:
        if raw_input("\nReally quit? (y/n)> ").lower().startswith('y'):
            sys.exit(1)

    except KeyboardInterrupt:
        print("Ok ok, quitting")
        sys.exit(1)

    # restore the exit gracefully handler here    
    signal.signal(signal.SIGINT, exit_gracefully)

if __name__ == '__main__':
    # store the original SIGINT handler
    original_sigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, exit_gracefully)
    main()