import unittest
from skewb import Skewb

class TestUnitRotations(unittest.TestCase):
	def test_front_turn(self):
		cube = Skewb()
		self.assertTrue(cube.is_solved())
		for _ in range(3):
			cube.move('F')
		self.assertTrue(cube.is_solved())
	
	def test_right_turn(self):
		cube = Skewb()
		self.assertTrue(cube.is_solved())
		for _ in range(3):
			cube.move('R')
		self.assertTrue(cube.is_solved())
	
	def test_left_turn(self):
		cube = Skewb()
		self.assertTrue(cube.is_solved())
		for _ in range(3):
			cube.move('L')
		self.assertTrue(cube.is_solved())

	def test_upper_turn(self):
		cube = Skewb()
		self.assertTrue(cube.is_solved())
		for _ in range(3):
			cube.move('U')
		self.assertTrue(cube.is_solved())

class TestIntegrationRotations(unittest.TestCase):
	def test_one_of_each_turn(self):
		cube = Skewb()
		self.assertTrue(cube.is_solved())
		cube.move('F')
		cube.move('R')
		cube.move('U')
		cube.move('L')
		expected_front = ['b', 'w', 'g', 'o', 'y']
		expected_up = ['r', 'g', 'w', 'y', 'o']
		expected_down = ['b', 'w', 'y', 'g', 'r']
		expected_left = ['b', 'o', 'o', 'w', 'y']
		expected_right = ['b', 'w', 'r', 'g', 'r']
		expected_back = ['o', 'y', 'b', 'g', 'r']
		self.assertListEqual(cube.front, expected_front)
		self.assertListEqual(cube.up, expected_up)
		self.assertListEqual(cube.down, expected_down)
		self.assertListEqual(cube.left, expected_left)
		self.assertListEqual(cube.right, expected_right)
		self.assertListEqual(cube.back, expected_back)

	def test_solve(self):
		cube = Skewb()
		self.assertTrue(cube.is_solved())
		cube.move('F')
		cube.move('F')
		cube.move('L')
		cube.move('F')
		cube.move('L')
		cube.move('L')
		cube.move('L')
		cube.move('F')
		cube.move('F')
		cube.move('L')
		cube.move('L')
		cube.move('F')
		self.assertTrue(cube.is_solved())

if __name__ == "__main__":
    unittest.main()