import gym
import gym_skewb

import numpy as np

env = gym.make('Skewb-v0')
env.reset(0)
for _ in range(4):
    env.render()
    observation, reward, done, info = env.step(env.action_space.sample()) 
    print(reward)