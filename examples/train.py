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
#env = make_vec_env(lambda: env, n_envs=1)
# Train the agent
#model = ACKTR('MlpPolicy', env, verbose=1).learn(5000)
model = DQN(MlpPolicy, env, verbose=1, 
        buffer_size=50000,
        learning_rate=0.01, 
        exploration_fraction=0.3,
        exploration_final_eps = 0.01, 
        learning_starts=1000, 
        target_network_update_freq=1000,
        gamma=0.99
    ).learn(total_timesteps=250000)

print("Saving...")
model.save("newmodel25000.pkl")

