import gym
import gym_skewb

from baselines import deepq
from baselines.common import set_global_seeds
from baselines import logger


class Train:
    def __init__(self, lr=0.001, seed=0, check_freq=10000, check_path="./skewb_model_checkpoint", timesteps=1000000):
        self.lr = lr # learning rate
        self.seed = seed
        self.check_freq = check_freq
        self.check_path = check_path
        self.timesteps = timesteps

    def callback(self, local, glbal):
        return bool(local['t'] > 100 and sum(local['episode_rewards'][-101:-1]) / 100 >= 0.95)

    def main(self):
        logger.configure()
        #set_global_seeds(self.seed)
        env = gym.make("Skewb-v0")

        print("pre learn")
        act = deepq.learn(
            env,
            network='mlp',
            lr=self.lr,
            total_timesteps=self.timesteps,
            buffer_size=50000,
            exploration_fraction=0.3,
            exploration_final_eps=0.01,
            print_freq=100,
            train_freq=4,
            learning_starts=10000,
            target_network_update_freq=1000,
            gamma=0.99,
            prioritized_replay=True,
            prioritized_replay_alpha=0.6,
            checkpoint_freq=self.check_freq,
            checkpoint_path=self.check_path,
            callback=self.callback
        )

        print("Saving...")
        act.save("skewbmodel.pkl")


if __name__ == '__main__':
    a = Train()
    a.main()
