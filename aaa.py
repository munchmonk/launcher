#!/usr/local/opt/python@3.8/bin/python3

import pygame
import sys


class Haunter(pygame.sprite.Sprite):
	def __init__(self, groups):
		pygame.sprite.Sprite.__init__(self, groups)

		self.image = pygame.image.load('haunter.png')
		self.rect = self.image.get_rect(topleft=(0, 0))

	def update(self):
		pass

	def draw(self):
		pass


class Square(pygame.sprite.Sprite):
	def __init__(self, x, y, groups):
		pygame.sprite.Sprite.__init__(self, groups)

		self.image = pygame.image.load('square.png')
		self.rect = self.image.get_rect(topleft=(x, y))

	def update(self):
		pass

	def draw(self):
		pass


class ScreenManager:
	def __init__(self):
		self._resolutions = pygame.display.list_modes()
		self._res_index = 0
		self._fullscreen = False

		self._aspect_ratio = None
		self._screen_surf = None

		self._set_screen_surf()
		self._update_aspect_ratio()

	def _set_screen_surf(self):
		self._screen_surf = pygame.display.set_mode(self._resolutions[self._res_index])
		self._update_aspect_ratio()

	def _update_aspect_ratio(self):
		self._aspect_ratio = self._resolutions[self._res_index][0] / self._resolutions[self._res_index][1]		

	def get_screen_surf(self):
		return self._screen_surf

	def is_fullscreen(self):
		return self._fullscreen

	def toggle_fullscreen(self):
		if self.is_fullscreen():
			pygame.display.set_mode(self._resolutions[self._res_index])
		else:
			# pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
			pygame.display.set_mode((self._resolutions[0]), pygame.FULLSCREEN)

		self._fullscreen = not self._fullscreen
		self._update_aspect_ratio()

	def enlarge_screen(self):
		if self.is_fullscreen():
			return
		if self._res_index == 0:
			return
		self._res_index -= 1
		self._set_screen_surf()

	def shrink_screen(self):
		if self.is_fullscreen():
			return
		if self._res_index == len(self._resolutions) - 1:
			return
		self._res_index += 1
		self._set_screen_surf()

	def reload(self):
		self.__init__()

	def show_info(self):
		print(self._resolutions)
		print(self._resolutions[self._res_index])
		# print(pygame.display.Info())
		print(self._aspect_ratio)


class Launcher:
	def __init__(self):
		self.screen_manager = ScreenManager()
		self.screen_surf = self.screen_manager.get_screen_surf()

		self.allsprites = pygame.sprite.Group()
		self.square = Square(0, 0, self.allsprites)
		self.square = Square(980, 500, self.allsprites)

	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.quit()

				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						self.quit()
					elif event.key == pygame.K_w:
						self.screen_manager.toggle_fullscreen()
					elif event.key == pygame.K_r:
						self.screen_manager.reload()
					elif event.key == pygame.K_p:
						self.screen_manager.enlarge_screen()
					elif event.key == pygame.K_o:
						self.screen_manager.shrink_screen()
					elif event.key == pygame.K_l:
						self.screen_manager.show_info()

			self.screen_surf.fill((0, 0, 255))
			self.allsprites.update()
			self.allsprites.draw(self.screen_surf)
			pygame.display.flip()

	def quit(self):
		pygame.quit()
		sys.exit()


if __name__ == '__main__':
	pygame.init()
	Launcher().run()








	