from numpy import array

'''
The whole picture is referred here as _matrix_.

'''

def get_neighbours(pixel,matrix):
	'''
	Returns a list of all neighbours for a given pixel. Neighbours are given by coordinates (i,j) that correspond to a position in a matrix.

	There can be not more than 8 (eight) neighbours for a pixel in total.
	'''
	a,b = pixel
	increment = [-1,0,1]
	list_of_neighbours = [ (a+i,b+j) for i in increment for j in increment if a+i >= 0 and a+i < len(matrix) and b+j >=0 and b+j <len(matrix[0])]
	list_of_neighbours.remove((a,b))

	return list_of_neighbours


def is_black(pixel,matrix):
	'''
	Checks if a pixel is black.
	'''
	a,b = pixel
	if matrix[a][b] == 1:
		return True
	return False

def explore_image(start_pixel,matrix):
	'''
	Finds all black pixels that belong to the current image.

	Returns two lists. A list with coordinates of the black pixels, and a list of pixels that have been checked.
	'''
	# initialise lists
	image = [start_pixel]	# a black image's pixels
	queue = [start_pixel]	# a queue of pixels to visit 
	checked_pixels = []
	while len(queue)>0:
		# take a pixel
		p =  queue[-1]
		# and remove it from the queue
		queue.pop()

		neighbours = get_neighbours(p,matrix)
		for pixel in neighbours:
			if is_black(pixel,matrix) and pixel not in image:
				queue.append(pixel)
				image.append(pixel)
		checked_pixels += neighbours

	return image, checked_pixels

def traverse_matrix(matrix):
	'''
	Checks all the pixels in a picture and finds all the black imagies.

	A group of black pixels are considered as a separate image they form a cluster surrounded by white pixels.
	'''
	n_of_images = 0
	# get a list of all pixels to visit in a format (i,j)
	not_visited_pixels = [(i,j) for i in range(len(matrix)) for j in range(len(matrix[0]))]
	print('There are total of ',len(not_visited_pixels),' pixels to visit.\n')

	while len(not_visited_pixels)>0:
		# take a pixel
		pixel = not_visited_pixels[0]
		# and remove it from the queue (list of not visited pixels)
		not_visited_pixels.remove(pixel)
		if is_black(pixel,matrix):
			print('I found a black image!')
			n_of_images += 1
			image, checked_pixels = explore_image(pixel,matrix)
			print('There are %s pixels in the image' % len(image))
			# remove visited pixels from the queue
			not_visited_pixels = [ _ for _ in not_visited_pixels if _ not in checked_pixels ]
			print('\nThere are ',len(not_visited_pixels),' pixels to visit left.\n')
	print('There were %s black images found in the picture.' % n_of_images)
	return None