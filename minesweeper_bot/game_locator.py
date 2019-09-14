import PIL
import pyautogui
from pynput import mouse
from PIL import ImageGrab


global coordinates
coordinates = []


def on_move(x, y):
	pass

def on_click(x, y, button, pressed):
	if pressed:
		coordinates.append(x)
		coordinates.append(y)
	if not pressed and len(coordinates)== 4:
		# Stop listener
		return False


def on_scroll(x, y, dx, dy):
	pass


def find_window():
	with mouse.Listener(
			on_move=on_move,
			on_click=on_click,
			on_scroll=on_scroll) as listener:
		listener.join()

	return coordinates


def get_image(bbox):
	return ImageGrab.grab(bbox)


