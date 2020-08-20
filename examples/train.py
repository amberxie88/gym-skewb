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
"""model = DQN(MlpPolicy, env, verbose=1, 
        buffer_size=25000,
        learning_rate=0.001, 
        exploration_fraction=0.3,
        exploration_final_eps = 0.01, 
        learning_starts=0, 
        target_network_update_freq=100,
        gamma=0.99
    ).learn(total_timesteps=25000)"""

model = DQN(MlpPolicy, env, verbose=1,
    ).learn(250000)

print(model.learning_rate)

print("Saving...")
model.save("model25000.pkl")

# Best was Learning 100, target 100, buffer 50k, lr 0.001, expl 0.3,
# expl final 0.01, gamma 0.99

# 1e-4 seems to be the best

