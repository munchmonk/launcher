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


class JoystickManager:
	PS2_NAME = 'Twin USB Joystick'

	PS2_LEFT_JOYSTICK, PS2_RIGHT_JOYSTICK = 0, 1
	UP_ARROW, DOWN_ARROW, LEFT_ARROW, RIGHT_ARROW = 0, 1, 2, 3

	(CROSS, SQUARE, TRIANGLE, CIRCLE, 
	START, SELECT,
	R1, R2, R3, L1, L2, L3) = range(12)

	PS2_HATS_MAP = 	   {0: PS2_RIGHT_JOYSTICK,
						1: PS2_LEFT_JOYSTICK
	}	

	PS2_BUTTONS_MAP =  {0:  (PS2_RIGHT_JOYSTICK, TRIANGLE),
						1:  (PS2_RIGHT_JOYSTICK, CIRCLE),
						2:  (PS2_RIGHT_JOYSTICK, CROSS),
						3:  (PS2_RIGHT_JOYSTICK, SQUARE),
						4:  (PS2_RIGHT_JOYSTICK, L2),
						5:  (PS2_RIGHT_JOYSTICK, R2),
						6:  (PS2_RIGHT_JOYSTICK, L1),
						7:  (PS2_RIGHT_JOYSTICK, R1),
						8:  (PS2_RIGHT_JOYSTICK, SELECT),
						9:  (PS2_RIGHT_JOYSTICK, START),
						10: (PS2_RIGHT_JOYSTICK, L3),
						11: (PS2_RIGHT_JOYSTICK, R3),
						12: (PS2_LEFT_JOYSTICK, TRIANGLE),
						13: (PS2_LEFT_JOYSTICK, CIRCLE),
						14: (PS2_LEFT_JOYSTICK, CROSS),
						15: (PS2_LEFT_JOYSTICK, SQUARE),
						16: (PS2_LEFT_JOYSTICK, L2),
						17: (PS2_LEFT_JOYSTICK, R2),
						18: (PS2_LEFT_JOYSTICK, L1),
						19: (PS2_LEFT_JOYSTICK, R1),
						20: (PS2_LEFT_JOYSTICK, SELECT),
						21: (PS2_LEFT_JOYSTICK, START),
						22: (PS2_LEFT_JOYSTICK, L3),
						23: (PS2_LEFT_JOYSTICK, R3)
	}


	def __init__(self):
		pygame.joystick.init()
		self.joysticks = []

		for i in range(pygame.joystick.get_count()):
			self.joysticks.append(pygame.joystick.Joystick(i))
			self.joysticks[i].init()
			print('Detected joystick \'' + self.joysticks[i].get_name() + '\'')

	def resolve_button_input(self, joystick_id, button_id):
		if self.joysticks[joystick_id].get_name() == JoystickManager.PS2_NAME:
			joystick, button = JoystickManager.PS2_BUTTONS_MAP[button_id][0], JoystickManager.PS2_BUTTONS_MAP[button_id][1]
			return joystick, button

		return None, None

	def resolve_hat_input(self, joystick_id, hat_id, value):
		if self.joysticks[joystick_id].get_name() == JoystickManager.PS2_NAME:
			joystick = JoystickManager.PS2_HATS_MAP[hat_id]

			arrow = None
			if value == (1, 0):
				arrow = JoystickManager.RIGHT_ARROW
			elif value == (0, 1):
				arrow = JoystickManager.UP_ARROW
			elif value == (-1, 0):
				arrow = JoystickManager.LEFT_ARROW
			elif value == (0, -1):
				arrow = JoystickManager.DOWN_ARROW

			return joystick, arrow

	def reload_joysticks(self):
		pygame.joystick.quit()
		self.__init__()


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
		self.joystick_manager = JoystickManager()

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
					elif event.key == pygame.K_j:
						self.joystick_manager.reload_joysticks()

				elif event.type == pygame.JOYBUTTONDOWN:
					joystick, button = self.joystick_manager.resolve_button_input(event.joy, event.button)
					if joystick == self.joystick_manager.PS2_LEFT_JOYSTICK:
						if button == self.joystick_manager.SQUARE:
							print('P1, left punch!')
						if button == self.joystick_manager.TRIANGLE:
							print('P1, right punch!')
					if joystick == self.joystick_manager.PS2_RIGHT_JOYSTICK:
						if button == self.joystick_manager.SQUARE:
							print('P2, left punch!')
						if button == self.joystick_manager.TRIANGLE:
							print('P2, right punch!')

				elif event.type == pygame.JOYHATMOTION:
					joystick, arrow = self.joystick_manager.resolve_hat_input(event.joy, event.hat, event.value)
					if joystick == self.joystick_manager.PS2_LEFT_JOYSTICK:
						if arrow == self.joystick_manager.UP_ARROW:
							print('P1, jump!')
					if joystick == self.joystick_manager.PS2_RIGHT_JOYSTICK:
						if arrow == self.joystick_manager.UP_ARROW:
							print('P2, jump!')					

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








	