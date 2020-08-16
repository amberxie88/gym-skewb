import gym
from gym import error, spaces, utils
from gym.utils import seeding

from sklearn.preprocessing import LabelBinarizer
from gym_skewb.envs import skewb

"""
actionList = ['R', 'r', 'L', 'l', 'U', 'F', 'D', 'B',
	'.R', '.r', '.L', '.l', '.U', '.F', '.D', '.B',]
"""

ACTION_LOOKUP = {
	0: 'F'
	1: 'R'
	2: 'L'
	3: 'U'
}

class SkewbEnv(gym.Env):

	def __init__(self):
		self.mySkewb = skewb.Skewb() #todo: Create Skewb
		self.action_space = spaces.Discrete(4)

		#No. of face * No. of possible color
		#self.observation_space = spaces.Tuple((spaces.Discrete(5*6), spaces.Discrete(8)))

		#LabelBinarizer to transform cube to array
		self.color_binarizer = LabelBinarizer()
		self.color_binarizer.fit(['[r]','[o]','[y]','[w]','[b]','[g]'])
		return

	def step(self, action):
		self._take_action(action)
		reward = self._get_reward()
		episode_over = self.mySkewb.is_solved() #todo: implement solved
		return self.get_state(), reward, episode_over, info_dict 

	def reset(self, step = 3):
		self.mySkewb = skewb.Skewb() #todo: Create Skewb
		for i in range(step):
			self.step(self.action_space.sample())
		return self.get_state()

	def render(self, mode='human', close=False):
		print("Rendering")
		print(self.get_state())
		return

	def get_state(self):
		return self.skewb.to_array() #todo: implement to_array

	def _take_action(self, action):
		self.mySkewb.move(ACTION_LOOKUP[action]) #todo: implement move

	def _get_reward(self):
		return np.mean(skewb.Skewb().to_array() == self.mySkewb.to_array()) #todo: implement reward


