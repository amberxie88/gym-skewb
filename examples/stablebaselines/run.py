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
#model = DQN.load("newmodel250000.pkl")
#model = DQN.load("basicmodel.pkl")
#model = DQN.load("currentbest.pkl")
model = DQN.load("skewbmodel.pkl")

# Test the trained agent
scramble_steps = 1
obs = env.reset(step=scramble_steps)
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
      # Note that the VecEnv resets automatically
      # when a done signal is encountered
      #print("Goal reached!", "reward=", reward)
      print("Goal reached in", step + 1, "steps")
      break
  if step + 1 == n_steps:
    print("Goal not reached")
    failures += 1
  print("Reward", total_reward)
  env.reset(step=scramble_steps)

print((iterations - failures) / iterations, "success")