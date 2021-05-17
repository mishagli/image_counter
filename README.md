# image_counter

A simple algorithm for detecting imagies in black and white pictures.

The following assumtions are made:
- Pictures are given by matrices in form of ones and zeros
- White pixels are zeros, and black pixels are ones.
- A black image in this case is any cluster of ones in a matrix
- - a cluster should be all surrounded by zeros (white pixels)
- - if a cluster has onye one black pixel it is still counter as an image.


## High-level description of the algorithm

- Input: a picture that contains black-and-white imagies is given by a matrix that contains ones (black pixels) and zeros (white pixels).
- `main()` function calls a subroutine `traverse_matrix()`
- `traverse_matrix()` iteratively checks pixels until all pixels are visited. When the black pixel is detectd, `explore_image()` is called.
-  - `explore_image()` starts from the detected black pixel and explores all its neighbours in Breadth-First Search manner until the whole black image is detected. It returns the image (a list of coordinates of black pixels) and all the pixels that were checked.
