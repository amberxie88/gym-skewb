from stable_baselines import DQN, PPO2, A2C, ACKTR
from stable_baselines.common.env_checker import check_env
from stable_baselines.common.cmd_util import make_vec_env
from stable_baselines.deepq.policies import MlpPolicy
from stable_baselines.common.vec_env import DummyVecEnv

import matplotlib.pyplot as plt
import numpy as np
import gym
import gym_skewb

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
    ).learn(total_timesteps=100000, log_interval=100)

print(model.learning_rate)

print("Saving...")
model.save("model.pkl")