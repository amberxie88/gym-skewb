import gym
from gym import error, spaces, utils
from gym.utils import seeding

class SkewbEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self):
  	return
    
  def step(self, action):
  	return state, reward, episode_over, info_dict 
    
  def reset(self):
  	return reset_state
    
  def render(self, mode='human', close=False):
    print()
    return