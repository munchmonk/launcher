#!/usr/local/opt/python@3.8/bin/python3

import pygame
import sys




class ScreenManager:
	def __init__(self):
		self._resolutions = pygame.display.list_modes()
		self._res_index = 0
		self._fullscreen = False

		self._screen_surf = None

		self._set_screen_surf()
		# self._screen_surf = pygame.display.set_mode(self._resolutions[self._res_index])

	def _set_screen_surf(self):
		self._screen_surf = pygame.display.set_mode(self._resolutions[self._res_index])		

	def get_screen_surf(self):
		return self._screen_surf

	def is_fullscreen(self):
		return self._fullscreen

	def toggle_fullscreen(self):
		if self.is_fullscreen():
			pygame.display.set_mode(self._resolutions[self._res_index])
		else:
			pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

		self._fullscreen = not self._fullscreen

	def enlarge_screen(self):
		if self._res_index == 0:
			return
		self._res_index -= 1
		self._set_screen_surf()

	def shrink_screen(self):
		if self._res_index == len(self._resolutions) - 1:
			return
		self._res_index += 1
		self._set_screen_surf()
	

class Launcher:
	def __init__(self):
		self.screen_manager = ScreenManager()
		self.screen_surf = self.screen_manager.get_screen_surf()

	def reload_screen_manager(self):
		self.screen_manager = ScreenManager()


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
						self.reload_screen_manager()
					elif event.key == pygame.K_p:
						self.screen_manager.enlarge_screen()
					elif event.key == pygame.K_o:
						self.screen_manager.shrink_screen()

			self.screen_surf.fill((0, 0, 255))
			pygame.display.flip()

	def quit(self):
		pygame.quit()
		sys.exit()


if __name__ == '__main__':
	pygame.init()
	Launcher().run()








	