from stable_baselines import DQN, PPO2, A2C, ACKTR
from stable_baselines.common.env_checker import check_env
from stable_baselines.common.cmd_util import make_vec_env
from stable_baselines.deepq.policies import MlpPolicy
from stable_baselines.common.vec_env import DummyVecEnv

import matplotlib.pyplot as plt
import numpy as np
import gym
import gym_skewb

# Create environment and load model
env = gym.make('Skewb-v0')
check_env(env, warn=True)
model = DQN.load("model.pkl")

# Test the trained agent
scramble_steps = 1
obs = env.reset(moves=scramble_steps)
#env.render()

iterations = 100
n_steps = 50
failures = 0
for _ in range(iterations):
  total_reward = 0
  for step in range(n_steps):
    action, _ = model.predict(obs, deterministic=True)
    #print("Step {}".format(step + 1))
    #print("Action: ", action)
    obs, reward, done, info = env.step(action)
    total_reward += reward
    #print('obs=', obs, 'reward=', reward, 'done=', done)
    #env.render(mode='console')
    if done:
      break
  if total_reward == 0:
    print("Goal not reached")
    failures += 1
  else: 
    print("Goal reached in", env.step_count, "steps")
  env.reset(moves=scramble_steps)

print(failures)
print((iterations - failures) / iterations, "success")