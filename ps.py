import sys
from pprint import pprint as pp
from pynput.keyboard import Key, Listener, Controller
import click
click.disable_unicode_literals_warning = True

def print_screen_png(fname):
	import numpy as np
	import pyautogui,cv2
	image = pyautogui.screenshot()
	image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
	cv2.imwrite(fname, image)

@click.command()
@click.option('-f', 	'--file_name', 			default = 'snap', 	help = 'File prefix.', required=True )

def start_loop(**kwargs):
	
	fn=kwargs.get('file_name')
	assert fn
	
	def on_press(key):
		global pid
		if key == Key.print_screen:
			print('{0} pressed'.format(key))
			pngfn='%s_%03d.png' % (fn,pid)
			print_screen_png(pngfn)
			print('Screenshot %d is saved to "%s"' % (pid, pngfn))
			pid +=1

	def on_release(key):
		if key == Key.esc:
			# Stop listener
			return False

	with Listener(
			on_press=on_press,
			on_release=on_release) as listener:
		listener.join()	
		
if __name__ == "__main__":
	pid=0
	start_loop()

