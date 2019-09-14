from game_locator import get_image, find_window
import matplotlib.pyplot as plt
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Programas\Tesseract-OCR\tesseract'

# http://minesweeperonline.com/#beginner


def read_state(coordinates, pix_size, n_h, n_l):

	bbox = (coordinates[0]+(n_l)*pix_size,
			coordinates[1]+ (n_h)*pix_size,
			coordinates[0]+(n_l+1)*pix_size,
			coordinates[1]+(n_h+1)*pix_size)

	image = get_image(bbox)

	return get_number(image)


def get_number(image):
	im = pytesseract.image_to_string(image, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
	return im

