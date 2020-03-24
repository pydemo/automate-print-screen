import sys
from pprint import pprint as pp
from pynput.keyboard import Key, Listener, Controller
from PIL import Image, ImageGrab

import click
click.disable_unicode_literals_warning = True

def print_screen(fname, itype="JPEG"):
	img = ImageGrab.grab()
	img.save(fname, itype, quality=100, subsampling=0)
	

@click.command()
@click.option('-f', 	'--file_name', 			default = 'snap', 	help = 'File prefix.', required=True )

def start_loop(**kwargs):
	
	fn=kwargs.get('file_name')
	assert fn
	
	def on_press(key):
		global pid
		if key == Key.print_screen:
			print('{0} pressed'.format(key))
			imgfn='%s_%03d.jpg' % (fn,pid)
			print_screen(imgfn)
			print('Screenshot %d is saved to "%s"' % (pid, imgfn))
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

