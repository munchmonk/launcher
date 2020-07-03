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
	SWITCH_PRO_CONTROLLER 	= 'Pro controller'
	JOYCON_LEFT_VERTICAL 	= 'Left joycon, vertical'
	JOYCON_LEFT_HORIZONTAL 	= 'Left joycon, horizontal'
	JOYCON_RIGHT_VERTICAL 	= 'Right joycon, vertical'
	JOYCON_RIGHT_HORIZONTAL = 'Right joycon, horizontal'
	PAIRED_JOYCONS 			= 'Paired joycons'

	A = 'A'
	B = 'B'
	X = 'X'
	Y = 'Y'
	PLUS = 'PLUS'
	MINUS = 'MINUS'
	HOME = 'HOME'
	SNAPSHOT = 'SNAPSHOT'
	R = 'R'
	ZR = 'ZR'
	R3 = 'R3'
	L = 'L'
	ZL = 'ZL'
	L3 = 'L3'
	SR = 'SR'
	SL = 'SL'
	LEFT_ARROW = 'LEFT_ARROW'
	UP_ARROW = 'UP_ARROW'
	RIGHT_ARROW = 'RIGHT_ARROW'
	DOWN_ARROW = 'DOWN_ARROW'

	BUTTON_MAP =   {SWITCH_PRO_CONTROLLER:     {0:  B,
												1:  A,
												2:  Y,
												3:  X,
												4: 	L,
												5:  R,
												6:  ZL,
												7:  ZR,
												8:  MINUS,
												9:  PLUS,
												10: L3,
												11: R3,
												12: HOME,
												13: SNAPSHOT
					},
					JOYCON_RIGHT_VERTICAL: 	   {0:  A,
												1:  X,
												2:  B,
												3:  Y,
												4: 	SL,
												5:  SR,
												9:  PLUS,
												11: R3,
												12: HOME,
												14: R,
												15: ZR
					},
					JOYCON_RIGHT_HORIZONTAL:   {0:  B,
												1:  A,
												2:  Y,
												3:  X,
												4: 	SL,
												5:  SR,
												9:  PLUS,
												11: R3,
												12: HOME,
												14: R,
												15: ZR
					},
					JOYCON_LEFT_VERTICAL:	   {0:  LEFT_ARROW,
												1:  DOWN_ARROW,
												2:  UP_ARROW,
												3:  RIGHT_ARROW,
												4: 	SL,
												5:  SR,
												8:  MINUS,
												10: L3,
												13: SNAPSHOT,
												14: L,
												15: ZL
					},
					JOYCON_LEFT_HORIZONTAL:    {0:  DOWN_ARROW,
												1:  RIGHT_ARROW,
												2:  LEFT_ARROW,
												3:  UP_ARROW,
												4: 	SL,
												5:  SR,
												8:  MINUS,
												10: L3,
												13: SNAPSHOT,
												14: L,
												15: ZL
					}
	}

	def __init__(self, name, *physical_joysticks):
		self.name = name
		self.physical_joysticks = [physical_joystick for physical_joystick in physical_joysticks]
		self.active = False

	def activate(self):
		self.active = True

	def deactivate(self):
		self.active = False

	def process_button(self, physical_joystick, button_id):
		if self.name != VirtualJoystick.PAIRED_JOYCONS:
			return VirtualJoystick.BUTTON_MAP[self.name][button_id]
		else:
			if physical_joystick.get_name() == JoystickManager.JOYCON_RIGHT_NAME:
				return VirtualJoystick.BUTTON_MAP[VirtualJoystick.JOYCON_RIGHT_VERTICAL][button_id]
			elif physical_joystick.get_name() == JoystickManager.JOYCON_LEFT_NAME:
				return VirtualJoystick.BUTTON_MAP[VirtualJoystick.JOYCON_LEFT_VERTICAL][button_id]
			
	def is_linked_to_physical_joystick(self, joystick):
		for physical_joystick in self.physical_joysticks:
			if physical_joystick == joystick:
				return True
		return False


class JoystickManager:
	# Physical names set by pygame
	SWITCH_PRO_NAME = 'Pro Controller'
	JOYCON_LEFT_NAME = 'Joy-Con (L)'
	JOYCON_RIGHT_NAME = 'Joy-Con (R)'

	PRIORITY_LIST =    [VirtualJoystick.SWITCH_PRO_CONTROLLER,
						VirtualJoystick.PAIRED_JOYCONS,
						VirtualJoystick.JOYCON_RIGHT_VERTICAL,
						VirtualJoystick.JOYCON_LEFT_VERTICAL
	]

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
		right_joycon, left_joycon = None, None

		for joystick in self.joysticks:
			if joystick.get_name() == JoystickManager.SWITCH_PRO_NAME:
				self.virtual_joysticks.append(VirtualJoystick(VirtualJoystick.SWITCH_PRO_CONTROLLER, joystick))

			elif joystick.get_name() == JoystickManager.JOYCON_RIGHT_NAME:
				self.virtual_joysticks.append(VirtualJoystick(VirtualJoystick.JOYCON_RIGHT_VERTICAL, joystick))
				self.virtual_joysticks.append(VirtualJoystick(VirtualJoystick.JOYCON_RIGHT_HORIZONTAL, joystick))
				right_joycon = joystick

			elif joystick.get_name() == JoystickManager.JOYCON_LEFT_NAME:
				self.virtual_joysticks.append(VirtualJoystick(VirtualJoystick.JOYCON_LEFT_VERTICAL, joystick))
				self.virtual_joysticks.append(VirtualJoystick(VirtualJoystick.JOYCON_LEFT_HORIZONTAL, joystick))
				left_joycon = joystick

		if right_joycon and left_joycon:
			self.virtual_joysticks.append(VirtualJoystick(VirtualJoystick.PAIRED_JOYCONS, right_joycon, left_joycon))

	def activate_first_joysticks(self):
		p1, p2 = None, None

		for priority_joystick in JoystickManager.PRIORITY_LIST:
			if p1 and p2:
				return p1, p2

			for virtual_joystick in self.virtual_joysticks:
				if virtual_joystick.name == priority_joystick:
					virtual_joystick.activate()
					if not p1:
						p1 = virtual_joystick
					else:
						p2 = virtual_joystick
		return p1, p2
							
	def _identify(self, joystick_id):
		return self.joysticks[joystick_id].get_name()

	def resolve_button_input(self, joystick_id, button_id):
		joystick, button = None, None
		physical_joystick = self.joysticks[joystick_id]

		for virtual_joystick in self.virtual_joysticks:
			if virtual_joystick.active and virtual_joystick.is_linked_to_physical_joystick(physical_joystick):
				joystick = virtual_joystick
				button = virtual_joystick.process_button(physical_joystick, button_id)
				# print(joystick.name + ' -> ' + str(button))

		return joystick, button

	# def resolve_hat_input(self, joystick_id, hat_id, value):
	# 	joystick, arrow = None, None

	# 	if self._identify(joystick_id) == JoystickManager.SWITCH_PRO_NAME:
	# 		joystick = JoystickManager.SWITCH_PRO_CONTROLLER

	# 		if value == (1, 0):
	# 			arrow = JoystickManager.RIGHT_ARROW
	# 		elif value == (0, 1):
	# 			arrow = JoystickManager.UP_ARROW
	# 		elif value == (-1, 0):
	# 			arrow = JoystickManager.LEFT_ARROW
	# 		elif value == (0, -1):
	# 			arrow = JoystickManager.DOWN_ARROW

	# 	elif self._identify(joystick_id) == JoystickManager.JOYCON_RIGHT_NAME:
	# 		joystick = JoystickManager.JOYCON_RIGHT

	# 		if value == (1, 0):
	# 			arrow = JoystickManager.UP_ARROW
	# 		elif value == (0, 1):
	# 			arrow = JoystickManager.LEFT_ARROW
	# 		elif value == (-1, 0):
	# 			arrow = JoystickManager.DOWN_ARROW
	# 		elif value == (0, -1):
	# 			arrow = JoystickManager.RIGHT_ARROW	

	# 	elif self._identify(joystick_id) == JoystickManager.JOYCON_LEFT_NAME:
	# 		joystick = JoystickManager.JOYCON_LEFT

	# 		if value == (1, 0):
	# 			arrow = JoystickManager.DOWN_ARROW
	# 		elif value == (0, 1):
	# 			arrow = JoystickManager.RIGHT_ARROW
	# 		elif value == (-1, 0):
	# 			arrow = JoystickManager.UP_ARROW
	# 		elif value == (0, -1):
	# 			arrow = JoystickManager.LEFT_ARROW

	# 	return joystick, arrow

	# def resolve_axis_input(self):
	# 	joysticks = []
	# 	axes = []
	# 	values = []

	# 	for joystick in self.joysticks:
	# 		if joystick.get_name() == JoystickManager.SWITCH_PRO_NAME:
	# 			for i in range(len(JoystickManager.SWITCH_PRO_AXIS_MAP)):
	# 				if abs(joystick.get_axis(i)) > JoystickManager.SWITCH_PRO_AXES_TOLERANCE:
	# 					joysticks.append(JoystickManager.SWITCH_PRO_NAME)
	# 					axes.append(i)
	# 					values.append(abs(joystick.get_axis(i)) / joystick.get_axis(i))
	# 					# values.append(joystick.get_axis(i))

	# 	return joysticks, axes, values

	def reload_joysticks(self):
		pygame.joystick.quit()
		self.__init__()

	def _find_joystick_by_name(self, name):
		for joystick in self.joysticks:
			if joystick.get_name() == name:
				return joystick
		return None

	# def _find_joystick_by_virtual_name(self, virtual_name):
	# 	if virtual_name == JoystickManager.SWITCH_PRO_CONTROLLER:
	# 		return self._find_joystick_by_name(JoystickManager.SWITCH_PRO_NAME)
	# 	elif virtual_name == JoystickManager.JOYCON_RIGHT:
	# 		return self._find_joystick_by_name(JoystickManager.JOYCON_RIGHT_NAME)
	# 	elif virtual_name == JoystickManager.JOYCON_LEFT:
	# 		return self._find_joystick_by_name(JoystickManager.JOYCON_LEFT_NAME)
	# 	elif virtual_name == JoystickManager.PAIRED_JOYCONS:
	# 		return self._find_joystick_by_name(JoystickManager.PAIRED_JOYCONS_NAME)

	# 	return None


	def select_joystick_configuration(self):
		options = {}
		opt_index = 0

		for virtual_joystick in self.virtual_joysticks:
			options[opt_index] = virtual_joystick
			opt_index += 1

		print('----------')
		for key in options.keys():
			print(str(key) + ': ' + options[key].name)
		print('----------')

		p1, p2 = -1, -1
		while p1 not in (options.keys()):
			try:
				p1 = int(input('    > P1 joystick: '))
			except ValueError:
				pass

		p1 = options[p1]

		keys_to_delete = []
		if p1.name in (VirtualJoystick.JOYCON_RIGHT_VERTICAL, VirtualJoystick.JOYCON_RIGHT_HORIZONTAL):
			for key in options.keys():
				if options[key].name in (VirtualJoystick.JOYCON_RIGHT_VERTICAL, VirtualJoystick.JOYCON_RIGHT_HORIZONTAL, VirtualJoystick.PAIRED_JOYCONS):
					keys_to_delete.append(key)
		elif p1.name in (VirtualJoystick.JOYCON_LEFT_VERTICAL, VirtualJoystick.JOYCON_LEFT_HORIZONTAL):
			for key in options.keys():
				if options[key].name in (VirtualJoystick.JOYCON_LEFT_VERTICAL, VirtualJoystick.JOYCON_LEFT_HORIZONTAL, VirtualJoystick.PAIRED_JOYCONS):
					keys_to_delete.append(key)
		elif p1.name == VirtualJoystick.PAIRED_JOYCONS:
			for key in options.keys():
				if options[key].name in    (VirtualJoystick.JOYCON_LEFT_VERTICAL, VirtualJoystick.JOYCON_LEFT_HORIZONTAL, 
											VirtualJoystick.JOYCON_RIGHT_VERTICAL, VirtualJoystick.JOYCON_RIGHT_HORIZONTAL, VirtualJoystick.PAIRED_JOYCONS):
					keys_to_delete.append(key)

		for key in keys_to_delete:
			del options[key]

		print('----------')
		for key in options.keys():
			print(str(key) + ': ' + options[key].name)
		print('----------')

		while p2 not in (options.keys()):
			try:
				p2 = int(input('    > P1 joystick: '))
			except ValueError:
				pass

		p2 = options[p2]
			
		for virtual_joystick in self.virtual_joysticks:
			virtual_joystick.deactivate()
		p1.activate()
		p2.activate()

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
		self.p1_joystick, self.p2_joystick = self.joystick_manager.activate_first_joysticks()

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
						self.p1_joystick, self.p2_joystick = self.joystick_manager.select_joystick_configuration()
					elif event.key == pygame.K_y:
						print(self.p1_joystick, self.p2_joystick)

				elif event.type == pygame.JOYBUTTONDOWN:
					virtual_joystick, button = self.joystick_manager.resolve_button_input(event.joy, event.button)
					if self.p1_joystick and self.p1_joystick == virtual_joystick:
						print('P1 using ' + virtual_joystick.name + ' -> ' + button)
					elif self.p2_joystick and self.p2_joystick == virtual_joystick:
						print('P2 using ' + virtual_joystick.name + ' -> ' + button)

				# elif event.type == pygame.JOYHATMOTION:
				# 	joystick, arrow = self.joystick_manager.resolve_hat_input(event.joy, event.hat, event.value)

				# 	if joystick == self.joystick_manager.SWITCH_PRO_CONTROLLER:
				# 		if arrow == self.joystick_manager.UP_ARROW:
				# 			print('P3, jump!')
				# 	elif joystick == self.joystick_manager.JOYCON_RIGHT:
				# 		if arrow == self.joystick_manager.UP_ARROW:
				# 			print('Red, jump!')
				# 	elif joystick == self.joystick_manager.JOYCON_LEFT:
				# 		if arrow == self.joystick_manager.UP_ARROW:
				# 			print('Blue, jump!')

				# joysticks, axes, values = self.joystick_manager.resolve_axis_input()
				# for i in range(len(joysticks)):
				# 	print(joysticks[i])
				# 	print(self.joystick_manager.SWITCH_PRO_AXIS_MAP[axes[i]])
				# 	print(values[i])

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























	