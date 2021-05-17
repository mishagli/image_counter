from numpy import array

from src.image_counter import traverse_matrix


matrix = array([
	[0,0,1,0,0,0,0,1,0,0],
	[0,1,0,0,0,1,0,1,0,0],
	[0,1,1,0,0,1,0,0,0,0],
	[0,1,0,0,0,1,0,0,1,0],
	[0,1,1,0,0,1,1,0,0,0]
	])


def main():
	'''
	The main function calls a traverse_matrix function to obtain a dictionary with black imagies in a picture.
	The picture is given by a matrix (a numpy.array) consist of 0s and 1s.
	'''

	print('The example matrix:\n')
	print(matrix)
	print('')

	traverse_matrix(matrix)


if __name__ == '__main__':
	main()



















