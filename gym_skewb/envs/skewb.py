class Skewb: 
	def __init__(self):
		self.front = ['g' for _ in range(5)]
		self.up = ['w' for _ in range(5)]
		self.down = ['y' for _ in range(5)]
		self.left = ['o' for _ in range(5)]
		self.right = ['r' for _ in range(5)]
		self.back = ['b' for _ in range(5)]

	def to_array(self):
		return [self.front, self.up, self.down, 
			self.left, self.right, self.back]

	def is_solved(self):
		for face in self.to_array():
			if len(set(face)) > 1:
				return False
		return True

	def move(self, move_id):
		if move_id == 'F':
			self._turn_front()
		elif move_id == 'R':
			self._turn_right()
		elif move_id == 'L':
			self._turn_left()
		elif move_id == 'U':
			self._turn_upper()

	def _turn_front(self):
		# First side of turn
		temp = self.up[0]
		self.up[0] = self.right[4]
		self.right[4] = self.front[3]
		self.front[3] = temp

		# Second side of turn
		temp = self.down[3]
		self.down[3] = self.left[0]
		self.left[0] = self.back[3]
		self.back[3] = temp

		temp = self.down[2]
		self.down[2] = self.left[2]
		self.left[2] = self.back[2]
		self.back[2] = temp		

		temp = self.down[1]
		self.down[1] = self.left[4]
		self.left[4] = self.back[4]
		self.back[4] = temp

		temp = self.down[0]
		self.down[0] = self.left[3]
		self.left[3] = self.back[1]
		self.back[1] = temp

	def _turn_right(self):
		# First side of turn
		temp = self.up[3]
		self.up[3] = self.back[4]
		self.back[4] = self.right[3]
		self.right[3] = temp

		# Second side of turn
		temp = self.front[0]
		self.front[0] = self.left[3]
		self.left[3] = self.down[4]
		self.down[4] = temp

		temp = self.front[2]
		self.front[2] = self.left[2]
		self.left[2] = self.down[2]
		self.down[2] = temp

		temp = self.front[3]
		self.front[3] = self.left[4]
		self.left[4] = self.down[3]
		self.down[3] = temp

		temp = self.front[4]
		self.front[4] = self.left[1]
		self.left[1] = self.down[0]
		self.down[0] = temp

	def _turn_left(self):
		# First side of turn
		temp = self.up[1]
		self.up[1] = self.front[4]
		self.front[4] = self.left[3]
		self.left[3] = temp

		# Second side of turn
		temp = self.right[1]
		self.right[1] = self.down[4]
		self.down[4] = self.back[4]
		self.back[4] = temp

		temp = self.right[2]
		self.right[2] = self.down[2]
		self.down[2] = self.back[2]
		self.back[2] = temp

		temp = self.right[3]
		self.right[3] = self.down[0]
		self.down[0] = self.back[0]
		self.back[0] = temp

		temp = self.right[4]
		self.right[4] = self.down[1]
		self.down[1] = self.back[3]
		self.back[3] = temp

	def _turn_upper(self):
		# First side of turn
		temp = self.up[4]
		self.up[4] = self.left[4]
		self.left[4] = self.back[3]
		self.back[3] = temp

		# Second side of turn
		temp = self.front[1]
		self.front[1] = self.down[3]
		self.down[3] = self.right[4]
		self.right[4] = temp

		temp = self.front[2]
		self.front[2] = self.down[2]
		self.down[2] = self.right[2]
		self.right[2] = temp

		temp = self.front[3] 
		self.front[3] = self.down[1]
		self.down[1] = self.right[0]
		self.right[0] = temp

		temp = self.front[4]
		self.front[4] = self.down[4]
		self.down[4] = self.right[3]
		self.right[3] = temp

