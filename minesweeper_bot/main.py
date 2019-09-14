import numpy as np
from game_locator import find_window, get_image
from read_game_state import read_state

def initialize(height, length):
	coordinates = find_window()

	image = get_image(coordinates)


	pix_height = image.size[0]/height
	pix_length = image.size[1]/length

	pix_size = (pix_height + pix_length)/2

	return coordinates, pix_size


def main():
	height = 9
	length = 9

	coords, pix_size = initialize(height, length)

	game_state = np.zeros([height, length]) + np.nan

	value = read_state(coordinates=coords,
	           pix_size=pix_size,
	           n_h=1,
	           n_l=0)

	print(value)

main()