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




class VirtualJoystick:
	def __init__(self, name):
		self.name = name

		






class JoystickManager:
	# Names set by pygame
	# PS2_NAME = 'Twin USB Joystick'
	SWITCH_PRO_NAME = 'Pro Controller'
	JOYCON_LEFT_NAME = 'Joy-Con (L)'
	JOYCON_RIGHT_NAME = 'Joy-Con (R)'

	# Name set by me
	PAIRED_JOYCONS_NAME = 'Paired joycons'

	# Arbitrary names - virtual joysticks
	# PS2_JOYSTICK_LEFT, PS2_JOYSTICK_RIGHT, SWITCH_PRO_CONTROLLER, JOYCON_LEFT, JOYCON_RIGHT, PAIRED_JOYCONS = range(6)
	SWITCH_PRO_CONTROLLER, JOYCON_LEFT, JOYCON_RIGHT, PAIRED_JOYCONS = range(4)

	UP_ARROW, DOWN_ARROW, LEFT_ARROW, RIGHT_ARROW = range(4)

	# (CROSS, SQUARE, TRIANGLE, CIRCLE, 
	# START, SELECT,
	# R1, R2, R3, L1, L2, L3) = range(12)

	(A, B, X, Y,
	PLUS, MINUS, HOME, SNAPSHOT,
	R, ZR, R3, L, ZL, L3,
	SR, SL) = range(16)

	LEFT_STICK_HORIZONTAL, LEFT_STICK_VERTICAL, RIGHT_STICK_HORIZONTAL, RIGHT_STICK_VERTICAL = range(4)

	# Mapping - do not change
	# PS2_HATS_MAP = 	   {0: PS2_JOYSTICK_RIGHT,
	# 					1: PS2_JOYSTICK_LEFT
	# }	

	# PS2_BUTTONS_MAP =  {0:  (PS2_JOYSTICK_RIGHT, TRIANGLE),
	# 					1:  (PS2_JOYSTICK_RIGHT, CIRCLE),
	# 					2:  (PS2_JOYSTICK_RIGHT, CROSS),
	# 					3:  (PS2_JOYSTICK_RIGHT, SQUARE),
	# 					4:  (PS2_JOYSTICK_RIGHT, L2),
	# 					5:  (PS2_JOYSTICK_RIGHT, R2),
	# 					6:  (PS2_JOYSTICK_RIGHT, L1),
	# 					7:  (PS2_JOYSTICK_RIGHT, R1),
	# 					8:  (PS2_JOYSTICK_RIGHT, SELECT),
	# 					9:  (PS2_JOYSTICK_RIGHT, START),
	# 					10: (PS2_JOYSTICK_RIGHT, L3),
	# 					11: (PS2_JOYSTICK_RIGHT, R3),
	# 					12: (PS2_JOYSTICK_LEFT, TRIANGLE),
	# 					13: (PS2_JOYSTICK_LEFT, CIRCLE),
	# 					14: (PS2_JOYSTICK_LEFT, CROSS),
	# 					15: (PS2_JOYSTICK_LEFT, SQUARE),
	# 					16: (PS2_JOYSTICK_LEFT, L2),
	# 					17: (PS2_JOYSTICK_LEFT, R2),
	# 					18: (PS2_JOYSTICK_LEFT, L1),
	# 					19: (PS2_JOYSTICK_LEFT, R1),
	# 					20: (PS2_JOYSTICK_LEFT, SELECT),
	# 					21: (PS2_JOYSTICK_LEFT, START),
	# 					22: (PS2_JOYSTICK_LEFT, L3),
	# 					23: (PS2_JOYSTICK_LEFT, R3)
	# }

	SWITCH_PRO_BUTTONS_MAP =   {0:  B,
								1:  A,
								2:  Y,
								3:  X,
								4:  L,
								5:  R,
								6:  ZL,
								7:  ZR,
								8:  MINUS,
								9:  PLUS,
								10: L3,
								11: R3,
								12: HOME,
								13: SNAPSHOT
	}

	SWITCH_PRO_AXIS_MAP =  {0: LEFT_STICK_HORIZONTAL,
							1: LEFT_STICK_VERTICAL,
							2: RIGHT_STICK_HORIZONTAL,
							3: RIGHT_STICK_VERTICAL
	}

	JOYCON_RIGHT_BUTTONS_MAP = {0:  A,
								1:  X,
								2:  B,
								3:  Y,
								4:  SL,
								5:  SR,
								9:  PLUS,
								11: R3,
								12: HOME,
								14: R,
								15: ZR
	}

	JOYCON_LEFT_BUTTONS_MAP =  {0:  LEFT_ARROW,
								1:  DOWN_ARROW,
								2:  UP_ARROW,
								3:  RIGHT_ARROW,
								4:  SL,
								5:  SR,
								8:  MINUS,
								10: L3,
								13: SNAPSHOT,
								14: L,
								15: ZL
	}

	# Arbitrary parameter
	SWITCH_PRO_AXES_TOLERANCE = 0.5


	def __init__(self):
		pygame.joystick.init()
		self.joysticks = []
		self.virtual_joysticks = []

		for i in range(pygame.joystick.get_count()):
			self.joysticks.append(pygame.joystick.Joystick(i))
			self.joysticks[i].init()
			# print('Detected joystick \'' + self.joysticks[i].get_name() + '\'')

		self.initialise_virtual_joysticks()

	def initialise_virtual_joysticks(self):
		if self._find_joystick_by_name(JoystickManager.SWITCH_PRO_NAME):
			self.virtual_joysticks.append(VirtualJoystick(JoystickManager.SWITCH_PRO_NAME))

		if self._find_joystick_by_name(JoystickManager.JOYCON_RIGHT_NAME):
			self.virtual_joysticks.append(VirtualJoystick(JoystickManager.JOYCON_RIGHT_NAME)
				
		if self._find_joystick_by_name(JoystickManager.JOYCON_LEFT_NAME):
			self.virtual_joysticks.append(VirtualJoystick(JoystickManager.JOYCON_LEFT_NAME)


	def _identify(self, joystick_id):
		return self.joysticks[joystick_id].get_name()

	def resolve_button_input(self, joystick_id, button_id):
		joystick, button = None, None
		# if self._identify(joystick_id) == JoystickManager.PS2_NAME:
		# 	joystick, button = JoystickManager.PS2_BUTTONS_MAP[button_id][0], JoystickManager.PS2_BUTTONS_MAP[button_id][1]

		if self._identify(joystick_id) == JoystickManager.SWITCH_PRO_NAME:
			joystick, button = JoystickManager.SWITCH_PRO_CONTROLLER, JoystickManager.SWITCH_PRO_BUTTONS_MAP[button_id]

		elif self._identify(joystick_id) == JoystickManager.JOYCON_RIGHT_NAME:
			joystick, button = JoystickManager.JOYCON_RIGHT, JoystickManager.JOYCON_RIGHT_BUTTONS_MAP[button_id]

		elif self._identify(joystick_id) == JoystickManager.JOYCON_LEFT_NAME:
			joystick, button = JoystickManager.JOYCON_LEFT, JoystickManager.JOYCON_LEFT_BUTTONS_MAP[button_id]

		return joystick, button

	def resolve_hat_input(self, joystick_id, hat_id, value):
		joystick, arrow = None, None

		# if self._identify(joystick_id) == JoystickManager.PS2_NAME:
		# 	joystick = JoystickManager.PS2_HATS_MAP[hat_id]

		# 	if value == (1, 0):
		# 		arrow = JoystickManager.RIGHT_ARROW
		# 	elif value == (0, 1):
		# 		arrow = JoystickManager.UP_ARROW
		# 	elif value == (-1, 0):
		# 		arrow = JoystickManager.LEFT_ARROW
		# 	elif value == (0, -1):
		# 		arrow = JoystickManager.DOWN_ARROW

		if self._identify(joystick_id) == JoystickManager.SWITCH_PRO_NAME:
			joystick = JoystickManager.SWITCH_PRO_CONTROLLER

			if value == (1, 0):
				arrow = JoystickManager.RIGHT_ARROW
			elif value == (0, 1):
				arrow = JoystickManager.UP_ARROW
			elif value == (-1, 0):
				arrow = JoystickManager.LEFT_ARROW
			elif value == (0, -1):
				arrow = JoystickManager.DOWN_ARROW

		elif self._identify(joystick_id) == JoystickManager.JOYCON_RIGHT_NAME:
			joystick = JoystickManager.JOYCON_RIGHT

			if value == (1, 0):
				arrow = JoystickManager.UP_ARROW
			elif value == (0, 1):
				arrow = JoystickManager.LEFT_ARROW
			elif value == (-1, 0):
				arrow = JoystickManager.DOWN_ARROW
			elif value == (0, -1):
				arrow = JoystickManager.RIGHT_ARROW	

		elif self._identify(joystick_id) == JoystickManager.JOYCON_LEFT_NAME:
			joystick = JoystickManager.JOYCON_LEFT

			if value == (1, 0):
				arrow = JoystickManager.DOWN_ARROW
			elif value == (0, 1):
				arrow = JoystickManager.RIGHT_ARROW
			elif value == (-1, 0):
				arrow = JoystickManager.UP_ARROW
			elif value == (0, -1):
				arrow = JoystickManager.LEFT_ARROW

		return joystick, arrow

	def resolve_axis_input(self):
		joysticks = []
		axes = []
		values = []

		for joystick in self.joysticks:
			if joystick.get_name() == JoystickManager.SWITCH_PRO_NAME:
				for i in range(len(JoystickManager.SWITCH_PRO_AXIS_MAP)):
					if abs(joystick.get_axis(i)) > JoystickManager.SWITCH_PRO_AXES_TOLERANCE:
						joysticks.append(JoystickManager.SWITCH_PRO_NAME)
						axes.append(i)
						values.append(abs(joystick.get_axis(i)) / joystick.get_axis(i))
						# values.append(joystick.get_axis(i))

		return joysticks, axes, values

	def reload_joysticks(self):
		pygame.joystick.quit()
		self.__init__()

	def _find_joystick_by_name(self, name):
		for joystick in self.joysticks:
			if joystick.get_name() == name:
				return joystick
		return None

	def _find_joystick_by_virtual_name(self, virtual_name):
		if virtual_name == JoystickManager.SWITCH_PRO_CONTROLLER:
			return self._find_joystick_by_name(JoystickManager.SWITCH_PRO_NAME)
		elif virtual_name == JoystickManager.JOYCON_RIGHT:
			return self._find_joystick_by_name(JoystickManager.JOYCON_RIGHT_NAME)
		elif virtual_name == JoystickManager.JOYCON_LEFT:
			return self._find_joystick_by_name(JoystickManager.JOYCON_LEFT_NAME)
		elif virtual_name == JoystickManager.PAIRED_JOYCONS:
			return self._find_joystick_by_name(JoystickManager.PAIRED_JOYCONS_NAME)

		return None


	def select_joystick_configuration(self):
		options = {}
		opt_index = 0

		print('----------')

		for joystick in self.joysticks:
			print(str(opt_index) + ': ' + joystick.get_name())
			if joystick.get_name() == JoystickManager.SWITCH_PRO_NAME:
				options[opt_index] = JoystickManager.SWITCH_PRO_CONTROLLER
			elif joystick.get_name() == JoystickManager.JOYCON_RIGHT_NAME:
				options[opt_index] = JoystickManager.JOYCON_RIGHT
			elif joystick.get_name() == JoystickManager.JOYCON_LEFT_NAME:
				options[opt_index] = JoystickManager.JOYCON_LEFT
			opt_index += 1

		if JoystickManager.JOYCON_RIGHT in options.values() and JoystickManager.JOYCON_LEFT in options.values():
			print(str(opt_index) + ': ' + JoystickManager.PAIRED_JOYCONS_NAME)
			options[opt_index] = JoystickManager.PAIRED_JOYCONS

		p1, p2 = -1, -1
		print('----------')
		while p1 not in range(len(options.keys())):
			try:
				p1 = int(input('    > P1 joystick: '))
			except ValueError:
				pass

		while p2 not in range(len(options.keys())) or p2 == p1:
			try:
				p2 = int(input('    > P2 joystick: '))
			except ValueError:
				pass

		p1 = self._find_joystick_by_virtual_name(options[p1])
		p2 = self._find_joystick_by_virtual_name(options[p2])
			
		return p1, p2
			
		


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
		self.p1_joystick, self.p2_joystick = self.joystick_manager.select_joystick_configuration()

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
					elif event.key == pygame.K_s:
						self.joystick_manager.select_joystick_configuration()

				elif event.type == pygame.JOYBUTTONDOWN:
					joystick, button = self.joystick_manager.resolve_button_input(event.joy, event.button)
					# if joystick == self.joystick_manager.PS2_JOYSTICK_LEFT:
					# 	if button == self.joystick_manager.SQUARE:
					# 		print('P1, left punch!')
					# 	elif button == self.joystick_manager.TRIANGLE:
					# 		print('P1, right punch!')
					# elif joystick == self.joystick_manager.PS2_JOYSTICK_RIGHT:
					# 	if button == self.joystick_manager.SQUARE:
					# 		print('P2, left punch!')
					# 	elif button == self.joystick_manager.TRIANGLE:
					# 		print('P2, right punch!')
					if joystick == self.joystick_manager.SWITCH_PRO_CONTROLLER:
						if button == self.joystick_manager.Y:
							print('P3, left punch!')
						elif button == self.joystick_manager.X:
							print('P3, right punch!')
					elif joystick == self.joystick_manager.JOYCON_RIGHT:
						if button == self.joystick_manager.Y:
							print('Red joycon, left punch!')
						elif button == self.joystick_manager.X:
							print('Red joycon, right punch!')
					elif joystick == self.joystick_manager.JOYCON_LEFT:
						if button == self.joystick_manager.UP_ARROW:
							print('Blue joycon, jump!')
						elif button == self.joystick_manager.DOWN_ARROW:
							print('Blue joycon, crouch!')

				elif event.type == pygame.JOYHATMOTION:
					joystick, arrow = self.joystick_manager.resolve_hat_input(event.joy, event.hat, event.value)
					# if joystick == self.joystick_manager.PS2_JOYSTICK_LEFT:
					# 	if arrow == self.joystick_manager.UP_ARROW:
					# 		print('P1, jump!')
					# elif joystick == self.joystick_manager.PS2_JOYSTICK_RIGHT:
					# 	if arrow == self.joystick_manager.UP_ARROW:
					# 		print('P2, jump!')
					if joystick == self.joystick_manager.SWITCH_PRO_CONTROLLER:
						if arrow == self.joystick_manager.UP_ARROW:
							print('P3, jump!')
					elif joystick == self.joystick_manager.JOYCON_RIGHT:
						if arrow == self.joystick_manager.UP_ARROW:
							print('Red, jump!')
					elif joystick == self.joystick_manager.JOYCON_LEFT:
						if arrow == self.joystick_manager.UP_ARROW:
							print('Blue, jump!')

				joysticks, axes, values = self.joystick_manager.resolve_axis_input()
				for i in range(len(joysticks)):
					print(joysticks[i])
					print(self.joystick_manager.SWITCH_PRO_AXIS_MAP[axes[i]])
					print(values[i])



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























	