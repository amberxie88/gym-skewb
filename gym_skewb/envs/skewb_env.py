import gym
from gym import error, spaces, utils
from gym.utils import seeding

from sklearn.preprocessing import LabelBinarizer
from gym_skewb.envs import skewb
import numpy as np


"""
actionList = ['R', 'r', 'L', 'l', 'U', 'F', 'D', 'B',
	'.R', '.r', '.L', '.l', '.U', '.F', '.D', '.B',]
"""

ACTION_LOOKUP = {
	0: 'F',
	1: 'R',
	2: 'L',
	3: 'U',
}

TILE_LOOKUP = {
	'r': 0,
	'o': 1,
	'y': 2, 
	'g': 3,
	'b': 4, 
	'w': 5,
}

class SkewbEnv(gym.Env):

	def __init__(self):
		self.mySkewb = skewb.Skewb() 
		self.action_space = spaces.Discrete(4)

		#No. of tiles * No. of faces
		low = np.array([0 for _ in range(5*6)])
		high = np.array([5 for _ in range(5*6)])
		self.observation_space = spaces.Box(low, high, dtype=np.uint8)

		#LabelBinarizer to transform cube to array
		self.color_binarizer = LabelBinarizer()
		self.color_binarizer.fit(['[r]','[o]','[y]','[w]','[b]','[g]'])
		return

	def step(self, action):
		self._take_action(action)
		reward = self._get_reward()
		episode_over = self.mySkewb.is_solved() 
		info_dict = {'classic': skewb.Skewb().to_array(), 'mine': self.mySkewb.to_array()}
		return self.get_state(), reward, episode_over, info_dict 

	def reset(self, step = 3):
		self.mySkewb = skewb.Skewb()
		for i in range(step):
			self.step(self.action_space.sample())
		return self.get_state()

	def render(self, mode='human', close=False):
		print("Rendering")
		print(self.mySkewb.to_array())
		return

	def get_state(self):
		return self.mySkewb.to_flat_int_array(TILE_LOOKUP)

	def _take_action(self, action):
		self.mySkewb.move(ACTION_LOOKUP[action]) 

	def _get_reward(self):
		return np.mean(np.array(skewb.Skewb().to_array()) == np.array(self.mySkewb.to_array()))


