import sys
from pprint import pprint as pp

def print_screen_png(fname):
	import numpy as np
	import pyautogui,cv2
	image = pyautogui.screenshot()
	image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
	cv2.imwrite(fname, image)

if __name__ == "__main__":
		

	pid=0
	from pynput.keyboard import Key, Listener, Controller
	KB = Controller()
	def on_press(key):
		global pid
		if key == Key.print_screen:
			print(ctrlon, '{0} pressed'.format(key))
			print_screen_png('test_%03d.png' % pid)
			pid +=1



	def on_release(key):
		global ctrlon
		if key == Key.esc:
			# Stop listener
			return False


	with Listener(
			on_press=on_press,
			on_release=on_release) as listener:
		listener.join()	
