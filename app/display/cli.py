from colorama import *

styles = {
		'Dim': Style.DIM,
		'Normal': Style.NORMAL,
		'Bright': Style.BRIGHT
		}

foreground_colors = {
		'Black': Fore.BLACK,
		'Red': Fore.RED,
		'Green': Fore.GREEN,
		'Yellow': Fore.YELLOW,
		'Blue': Fore.BLUE,
		'Magenta': Fore.MAGENTA,
		'Cyan': Fore.CYAN,
		'White': Fore.WHITE
		}

background_colors = {
		'Black': Back.BLACK,
		'Red': Back.RED,
		'Green': Back.GREEN,
		'Yellow': Back.YELLOW,
		'Blue': Back.BLUE,
		'Magenta': Back.MAGENTA,
		'Cyan': Back.CYAN,
		'White': Back.WHITE
		}

def style_paint(style, text):
	opt = styles[style]
	print(opt + text)

def style_reset():
	print(Style.RESET_ALL)

def background_paint(color, text):
	opt = background_colors[color]
	print(opt + text)

def background_reset():
	print(Back.RESET)

def foreground_paint(color, text):
	opt = foreground_colors[color]
	print(opt + text)

def foreground_reset():
	print(Fore.RESET)
