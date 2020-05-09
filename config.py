import os
import pygame as pg
from math import ceil
from tkinter import Tk

def load_image(img, rez, alpha=True, crop=False):
	img = pg.image.load(img)
	if crop:
		w, h = img.get_size()
		# увеличиваем изначальную картинку, если по одной из сторон она меньше
		if rez[0] > w or rez[1] > h:
			scale = max(rez[0] / w, rez[1] / h)
			img = pg.transform.scale(img, (ceil(w * scale), ceil(h * scale)))
			w, h = img.get_size()
		# уменьшаем изначальную картинку, если по обеим сторонам она больше
		if w > rez[0] and h > rez[1]:
			scale = max(rez[0] / w, rez[1] / h)
			img = pg.transform.scale(img, (ceil(w * scale), ceil(h * scale)))
			w, h = img.get_size()
		# обрезаем излишки
		img = img.subsurface((0, 0, *rez))

	img = pg.transform.scale(img, rez)
	if alpha:
		img.convert_alpha()
	else:
		img.convert()
	return img

temp = Tk()
SCREEN = temp.winfo_screenwidth(), temp.winfo_screenheight()
del temp

SCALE = 50
WINSIZE = W, H = 9 * SCALE, 16 * SCALE
FPS = 60

WIN_COORDS = (SCREEN[0] - W) // 2, (SCREEN[1] - H) // 2

current_dir = os.path.dirname(__file__)
textures = os.path.join(current_dir, 'textures')
BG = os.path.join(textures, 'bg.jpg')