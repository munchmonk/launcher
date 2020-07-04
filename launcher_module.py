#!/usr/local/opt/python@3.8/bin/python3

import pygame
import sys
import os

sys.path.append('./pong')

import pong_module


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
	# Pro controller -> balls = axes, arrows = hats, rest = buttons
	# Joycons -> balls = hats, rest = buttons (including the arrows)

	# Virtual, arbitrary names
	SWITCH_PRO_CONTROLLER 	= 'Pro controller'
	JOYCON_LEFT_VERTICAL 	= 'Left joycon, vertical'
	JOYCON_LEFT_HORIZONTAL 	= 'Left joycon, horizontal'
	JOYCON_RIGHT_VERTICAL 	= 'Right joycon, vertical'
	JOYCON_RIGHT_HORIZONTAL = 'Right joycon, horizontal'
	PAIRED_JOYCONS 			= 'Paired joycons'

	# Pro controller (physical buttons) and joycon (physical buttons) buttons
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

	# Pro controller (physical hats) and joycons (physical buttons) arrows
	LEFT_ARROW = 'LEFT_ARROW'
	UP_ARROW = 'UP_ARROW'
	RIGHT_ARROW = 'RIGHT_ARROW'
	DOWN_ARROW = 'DOWN_ARROW'

	# Pro controller arrows (physical hats)
	NEUTRAL_ARROW = 'NEUTRAL_ARROW'
	UP_RIGHT_ARROW = 'UP_RIGHT_ARROW'
	DOWN_RIGHT_ARROW = 'DOWN_RIGHT_ARROW'
	DOWN_LEFT_ARROW = 'DOWN_LEFT_ARROW'
	UP_LEFT_ARROW = 'UP_LEFT_ARROW'

	# Pro controller (physical axes) and joycons (physical hats) balls
	RIGHT_SIDE_BALL = 'RIGHT_SIDE_BALL'
	LEFT_SIDE_BALL = 'LEFT_SIDE_BALL'
	HORIZONTAL_AXIS = 'HORIZONTAL_AXIS'
	VERTICAL_AXIS = 'VERTICAL_AXIS'

	# Ball states (joycons physical hat)
	BALL_NEUTRAL = 'BALL_NEUTRAL'
	BALL_UP = 'BALL_UP'
	BALL_UP_RIGHT = 'BALL_UP_RIGHT'
	BALL_RIGHT = 'BALL_RIGHT'
	BALL_DOWN_RIGHT = 'BALL_DOWN_RIGHT'
	BALL_DOWN = 'BALL_DOWN'
	BALL_DOWN_LEFT = 'BALL_DOWN_LEFT'
	BALL_LEFT = 'BALL_LEFT'
	BALL_UP_LEFT = 'BALL_UP_LEFT'

	# Physical map - do not change
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
					JOYCON_RIGHT_HORIZONTAL:   {0:  A,
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

	# Physical map - do not change
	HAT_MAP = {JOYCON_RIGHT_VERTICAL:  {(0, 0):		BALL_NEUTRAL,
										(1, 0): 	BALL_UP,
										(1, -1):	BALL_UP_RIGHT,
										(0, -1):	BALL_RIGHT,
										(-1, -1): 	BALL_DOWN_RIGHT,
										(-1, 0):	BALL_DOWN,
										(-1, 1):	BALL_DOWN_LEFT,
										(0, 1): 	BALL_LEFT,
										(1, 1): 	BALL_UP_LEFT
			 },
			 JOYCON_RIGHT_HORIZONTAL:  {(0, 0):		BALL_NEUTRAL,
										(1, 0): 	BALL_RIGHT,
										(1, -1):	BALL_DOWN_RIGHT,
										(0, -1):	BALL_DOWN,
										(-1, -1): 	BALL_DOWN_LEFT,
										(-1, 0):	BALL_LEFT,
										(-1, 1):	BALL_UP_LEFT,
										(0, 1): 	BALL_UP,
										(1, 1): 	BALL_UP_RIGHT
			},
			 JOYCON_LEFT_VERTICAL: 	   {(0, 0):		BALL_NEUTRAL,
										(1, 0): 	BALL_DOWN,
										(1, -1):	BALL_DOWN_LEFT,
										(0, -1):	BALL_LEFT,
										(-1, -1): 	BALL_UP_LEFT,
										(-1, 0):	BALL_UP,
										(-1, 1):	BALL_UP_RIGHT,
										(0, 1): 	BALL_RIGHT,
										(1, 1): 	BALL_DOWN_RIGHT
			},
			JOYCON_LEFT_HORIZONTAL:    {(0, 0):		BALL_NEUTRAL,
										(1, 0): 	BALL_RIGHT,
										(1, -1):	BALL_DOWN_RIGHT,
										(0, -1):	BALL_DOWN,
										(-1, -1): 	BALL_DOWN_LEFT,
										(-1, 0):	BALL_LEFT,
										(-1, 1):	BALL_UP_LEFT,
										(0, 1): 	BALL_UP,
										(1, 1): 	BALL_UP_RIGHT
			},
			SWITCH_PRO_CONTROLLER:	   {(0, 0): 	NEUTRAL_ARROW,
										(0, 1):		UP_ARROW,
										(1, 1):		UP_RIGHT_ARROW,
										(1, 0):		RIGHT_ARROW,
										(1, -1):	DOWN_RIGHT_ARROW,
										(0, -1):	DOWN_ARROW,
										(-1, -1):	DOWN_LEFT_ARROW,
										(-1, 0):	LEFT_ARROW,
										(-1, 1):	UP_LEFT_ARROW
			}
	}

	# Switch pro controller physical map - do not change
	LEFT_SIDE_BALL_HORIZONTAL_AXIS = 0
	LEFT_SIDE_BALL_VERTICAL_AXIS = 1
	RIGHT_SIDE_BALL_HORIZONTAL_AXIS = 2
	RIGHT_SIDE_BALL_VERTICAL_AXIS = 3	

	def __init__(self, name, *physical_joysticks):
		self.name = name
		self.physical_joysticks = [physical_joystick for physical_joystick in physical_joysticks]
		self.active = False

	def is_active(self):
		return self.active

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

	def process_hat(self, physical_joystick, value):
		hat, side = None, None

		if physical_joystick.get_name() == JoystickManager.JOYCON_RIGHT_NAME:
			if self.name == VirtualJoystick.JOYCON_RIGHT_VERTICAL:
				hat = VirtualJoystick.HAT_MAP[VirtualJoystick.JOYCON_RIGHT_VERTICAL][value]
			elif self.name == VirtualJoystick.JOYCON_RIGHT_HORIZONTAL:
				hat = VirtualJoystick.HAT_MAP[VirtualJoystick.JOYCON_RIGHT_HORIZONTAL][value]
			elif self.name == VirtualJoystick.PAIRED_JOYCONS:
				hat = VirtualJoystick.HAT_MAP[VirtualJoystick.JOYCON_RIGHT_VERTICAL][value]
				side = VirtualJoystick.RIGHT_SIDE_BALL

		elif physical_joystick.get_name() == JoystickManager.JOYCON_LEFT_NAME:
			if self.name == VirtualJoystick.JOYCON_LEFT_VERTICAL:
				hat = VirtualJoystick.HAT_MAP[VirtualJoystick.JOYCON_LEFT_VERTICAL][value]
			elif self.name == VirtualJoystick.JOYCON_LEFT_HORIZONTAL:
				hat = VirtualJoystick.HAT_MAP[VirtualJoystick.JOYCON_LEFT_HORIZONTAL][value]
			elif self.name == VirtualJoystick.PAIRED_JOYCONS:
				hat = VirtualJoystick.HAT_MAP[VirtualJoystick.JOYCON_LEFT_VERTICAL][value]
				side = VirtualJoystick.LEFT_SIDE_BALL

		elif physical_joystick.get_name() == JoystickManager.SWITCH_PRO_NAME:
			hat = VirtualJoystick.HAT_MAP[VirtualJoystick.SWITCH_PRO_CONTROLLER][value]

		return hat, side
			
	def is_linked_to_physical_joystick(self, joystick):
		for physical_joystick in self.physical_joysticks:
			if physical_joystick == joystick:
				return True
		return False


class Controller(pygame.sprite.Sprite):
	def __init__(self, screen_surf, options):
		pygame.sprite.Sprite.__init__(self)

		self.screen_surf = screen_surf
		self.controller_index = 0
		self.options = options
		self.images = []
		self.initialise_images()

		self.image = self.images[self.controller_index]
		self.rect = self.image.get_rect()

		self.recenter()

	def initialise_images(self):
		for virtual_joystick in self.options:
			if virtual_joystick.name == VirtualJoystick.SWITCH_PRO_CONTROLLER:
				self.images.append(pygame.image.load('pro_controller.jpg'))
			elif virtual_joystick.name == VirtualJoystick.JOYCON_RIGHT_HORIZONTAL:
				self.images.append(pygame.image.load('red_joycon_horizontal.jpg'))
			elif virtual_joystick.name == VirtualJoystick.JOYCON_RIGHT_VERTICAL:
				self.images.append(pygame.image.load('red_joycon_vertical.jpg'))
			elif virtual_joystick.name == VirtualJoystick.JOYCON_LEFT_HORIZONTAL:
				self.images.append(pygame.image.load('blue_joycon_horizontal.jpg'))
			elif virtual_joystick.name == VirtualJoystick.JOYCON_LEFT_VERTICAL:
				self.images.append(pygame.image.load('blue_joycon_vertical.jpg'))
			elif virtual_joystick.name == VirtualJoystick.PAIRED_JOYCONS:
				self.images.append(pygame.image.load('paired_joycons.jpg'))
			else:
				print('Error - no image for ' + virtual_joystick.name)
				pygame.quit()
				sys.exit()

	def recenter(self):
		self.rect.centerx = self.screen_surf.get_width() // 2
		self.rect.centery = self.screen_surf.get_height() // 2

	def next_controller(self):
		self.controller_index = (self.controller_index + 1) % len(self.images)
		self.image = self.images[self.controller_index]
		self.rect = self.image.get_rect()

		self.recenter()

	def previous_controller(self):
		self.controller_index = (self.controller_index - 1) % len(self.images)
		self.image = self.images[self.controller_index]
		self.rect = self.image.get_rect()

		self.recenter()

	def get_controller_type(self):
		return self.options[self.controller_index]

	def draw(self):
		self.screen_surf.fill((0, 0, 0))
		self.screen_surf.blit(JoystickManager.JOYSTICK_SELECTION_BACKGROUND_IMAGE, (0, 0))
		self.screen_surf.blit(self.image, self.rect)
		pygame.display.flip()


class JoystickManager:
	# Physical names set by pygame
	SWITCH_PRO_NAME = 'Pro Controller'
	JOYCON_LEFT_NAME = 'Joy-Con (L)'
	JOYCON_RIGHT_NAME = 'Joy-Con (R)'

	SWITCH_PRO_AXES_TOLERANCE = 0.5

	PRIORITY_LIST =    [VirtualJoystick.SWITCH_PRO_CONTROLLER,
						VirtualJoystick.PAIRED_JOYCONS,
						VirtualJoystick.JOYCON_RIGHT_HORIZONTAL,
						VirtualJoystick.JOYCON_LEFT_HORIZONTAL,
						VirtualJoystick.JOYCON_RIGHT_VERTICAL,
						VirtualJoystick.JOYCON_LEFT_VERTICAL
	]

	JOYSTICK_SELECTION_BACKGROUND_IMAGE = pygame.image.load(os.path.join(os.path.dirname(__file__), 'joystick_selection_background.png'))

	def __init__(self):
		self.joysticks = []
		self.virtual_joysticks = []

		self.initialise_joysticks()

	def initialise_joysticks(self):
		pygame.joystick.quit()
		pygame.joystick.init()
		self.initialise_physical_joysticks()
		self.initialise_virtual_joysticks()

	def initialise_physical_joysticks(self):
		self.joysticks = []

		for i in range(pygame.joystick.get_count()):
			self.joysticks.append(pygame.joystick.Joystick(i))
			self.joysticks[i].init()
			# print('Detected joystick \'' + self.joysticks[i].get_name() + '\'')

	def initialise_virtual_joysticks(self):
		self.virtual_joysticks = []
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
			if virtual_joystick.is_active() and virtual_joystick.is_linked_to_physical_joystick(physical_joystick):
				joystick = virtual_joystick
				button = virtual_joystick.process_button(physical_joystick, button_id)
				# print(joystick.name + ' -> ' + str(button))

		return joystick, button

	def resolve_hat_input(self, joystick_id, value):
		joystick, hat, side = None, None, None
		physical_joystick = self.joysticks[joystick_id]

		for virtual_joystick in self.virtual_joysticks:
			if virtual_joystick.is_active() and virtual_joystick.is_linked_to_physical_joystick(physical_joystick):
				joystick = virtual_joystick
				hat, side = virtual_joystick.process_hat(physical_joystick, value)

				return joystick, hat, side

		return joystick, hat, side

	def resolve_axes(self, joystick):
		if joystick.get_name() != JoystickManager.SWITCH_PRO_NAME:
			return None, None, None

		sides = [VirtualJoystick.RIGHT_SIDE_BALL, VirtualJoystick.LEFT_SIDE_BALL]
		balls = [None, None]

		for virtual_joystick in self.virtual_joysticks:
			if virtual_joystick.is_active() and virtual_joystick.is_linked_to_physical_joystick(joystick):
				# Right ball
				vertical_axis = joystick.get_axis(VirtualJoystick.RIGHT_SIDE_BALL_VERTICAL_AXIS)
				horizontal_axis = joystick.get_axis(VirtualJoystick.RIGHT_SIDE_BALL_HORIZONTAL_AXIS)
				
				if abs(vertical_axis) > JoystickManager.SWITCH_PRO_AXES_TOLERANCE:
					if vertical_axis > 0:
						balls[0] = VirtualJoystick.BALL_DOWN
					else:
						balls[0] = VirtualJoystick.BALL_UP

				if abs(horizontal_axis) > JoystickManager.SWITCH_PRO_AXES_TOLERANCE:
					if horizontal_axis > 0:
						if balls[0] == VirtualJoystick.BALL_UP:
							balls[0] = VirtualJoystick.BALL_UP_RIGHT
						elif balls[0] == VirtualJoystick.BALL_DOWN:
							balls[0] = VirtualJoystick.BALL_DOWN_RIGHT
						else:
							balls[0] = VirtualJoystick.BALL_RIGHT
					else:
						if balls[0] == VirtualJoystick.BALL_UP:
							balls[0] = VirtualJoystick.BALL_UP_LEFT
						elif balls[0] == VirtualJoystick.BALL_DOWN:
							balls[0] = VirtualJoystick.BALL_DOWN_LEFT
						else:
							balls[0] = VirtualJoystick.BALL_LEFT

				# Left ball
				vertical_axis = joystick.get_axis(VirtualJoystick.LEFT_SIDE_BALL_VERTICAL_AXIS)
				horizontal_axis = joystick.get_axis(VirtualJoystick.LEFT_SIDE_BALL_HORIZONTAL_AXIS)
				
				if abs(vertical_axis) > JoystickManager.SWITCH_PRO_AXES_TOLERANCE:
					if vertical_axis > 0:
						balls[1] = VirtualJoystick.BALL_DOWN
					else:
						balls[1] = VirtualJoystick.BALL_UP

				if abs(horizontal_axis) > JoystickManager.SWITCH_PRO_AXES_TOLERANCE:
					if horizontal_axis > 0:
						if balls[1] == VirtualJoystick.BALL_UP:
							balls[1] = VirtualJoystick.BALL_UP_RIGHT
						elif balls[1] == VirtualJoystick.BALL_DOWN:
							balls[1] = VirtualJoystick.BALL_DOWN_RIGHT
						else:
							balls[1] = VirtualJoystick.BALL_RIGHT
					else:
						if balls[1] == VirtualJoystick.BALL_UP:
							balls[1] = VirtualJoystick.BALL_UP_LEFT
						elif balls[1] == VirtualJoystick.BALL_DOWN:
							balls[1] = VirtualJoystick.BALL_DOWN_LEFT
						else:
							balls[1] = VirtualJoystick.BALL_LEFT

				return virtual_joystick, balls, sides
		return None, None, None

	def reload_joysticks(self):
		pygame.joystick.quit()
		self.__init__()

	def _find_joystick_by_name(self, name):
		for joystick in self.joysticks:
			if joystick.get_name() == name:
				return joystick
		return None

	def select_joystick_configuration(self, screen_surf):
		self.initialise_joysticks()

		options = []
		for virtual_joystick in self.virtual_joysticks:
			options.append(virtual_joystick)
			
		if not options:
			print('No joysticks found!')
			return None, None

		controller_sprite = Controller(screen_surf, options)

		p1, p2 = None, None

		while p1 not in options:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						pygame.quit()
						sys.exit()
					elif event.key == pygame.K_RIGHT:
						controller_sprite.next_controller()
					elif event.key == pygame.K_LEFT:
						controller_sprite.previous_controller()
					elif event.key == pygame.K_SPACE:
						p1 = controller_sprite.get_controller_type()
			controller_sprite.draw()

		options_to_remove = []
		if p1.name in (VirtualJoystick.JOYCON_RIGHT_VERTICAL, VirtualJoystick.JOYCON_RIGHT_HORIZONTAL):
			for option in options:
				if option.name in (VirtualJoystick.JOYCON_RIGHT_VERTICAL, VirtualJoystick.JOYCON_RIGHT_HORIZONTAL, VirtualJoystick.PAIRED_JOYCONS):
					options_to_remove.append(option)
		elif p1.name in (VirtualJoystick.JOYCON_LEFT_VERTICAL, VirtualJoystick.JOYCON_LEFT_HORIZONTAL):
			for option in options:
				if option.name in (VirtualJoystick.JOYCON_LEFT_VERTICAL, VirtualJoystick.JOYCON_LEFT_HORIZONTAL, VirtualJoystick.PAIRED_JOYCONS):
					options_to_remove.append(option)
		elif p1.name == VirtualJoystick.PAIRED_JOYCONS:
			for option in options:
				if option.name in  (VirtualJoystick.JOYCON_LEFT_VERTICAL, VirtualJoystick.JOYCON_LEFT_HORIZONTAL, 
									VirtualJoystick.JOYCON_RIGHT_VERTICAL, VirtualJoystick.JOYCON_RIGHT_HORIZONTAL, VirtualJoystick.PAIRED_JOYCONS):
					options_to_remove.append(option)
		elif p1.name == VirtualJoystick.SWITCH_PRO_CONTROLLER:
			for option in options:
				if option.name == VirtualJoystick.SWITCH_PRO_CONTROLLER:
					options_to_remove.append(option)

		for option in options_to_remove:
			options.remove(option)

		if options:
			controller_sprite.kill()
			controller_sprite = Controller(screen_surf, options)

			while p2 not in options:
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.quit()
						sys.exit()
					elif event.type == pygame.KEYDOWN:
						if event.key == pygame.K_ESCAPE:
							pygame.quit()
							sys.exit()
						elif event.key == pygame.K_RIGHT:
							controller_sprite.next_controller()
						elif event.key == pygame.K_LEFT:
							controller_sprite.previous_controller()
						elif event.key == pygame.K_SPACE:
							p2 = controller_sprite.get_controller_type()
				controller_sprite.draw()
		else:
			print('No more joysticks left for P2!')

		for virtual_joystick in self.virtual_joysticks:
			virtual_joystick.deactivate()

		p1.activate()
		if p2:
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

	def toggle_fullscreen(self, sprites=None):
		if self.is_fullscreen():
			pygame.display.set_mode(self._resolutions[self._res_index])
		else:
			# pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
			pygame.display.set_mode((self._resolutions[0]), pygame.FULLSCREEN)

		self._fullscreen = not self._fullscreen
		self._update_aspect_ratio()
		if sprites:
			self.recenter(sprites)

	def enlarge_screen(self, sprites=None):
		if self.is_fullscreen():
			return
		if self._res_index == 0:
			return
		self._res_index -= 1
		self._set_screen_surf()
		if sprites:
			self.recenter(sprites)

	def shrink_screen(self, sprites=None):
		if self.is_fullscreen():
			return
		if self._res_index == len(self._resolutions) - 1:
			return
		self._res_index += 1
		self._set_screen_surf()
		if sprites:
			self.recenter(sprites)

	def recenter(self, sprites):
		for sprite in sprites:
			sprite.recenter()

	def reload(self):
		self.__init__()

	def show_info(self):
		print(self._resolutions)
		print(self._resolutions[self._res_index])
		# print(pygame.display.Info())
		print(self._aspect_ratio)


class Launcher:
	FPS = 45
	BACKGROUND_IMAGE = pygame.image.load(os.path.join(os.path.dirname(__file__), 'background.png'))

	def __init__(self):
		self.screen_manager = ScreenManager()
		self.screen_surf = self.screen_manager.get_screen_surf()
		self.joystick_manager = JoystickManager()
		self.p1_joystick, self.p2_joystick = self.joystick_manager.activate_first_joysticks()

		self.allsprites = pygame.sprite.Group()
		# self.square = Square(0, 0, self.allsprites)
		# self.square = Square(980, 500, self.allsprites)
		self.background_image = Launcher.BACKGROUND_IMAGE
		self.clock = pygame.time.Clock()
		self.dt = 0

		pygame.mouse.set_visible(False)

	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.quit()

				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						self.quit()
					elif event.key == pygame.K_w:
						self.screen_manager.toggle_fullscreen(self.allsprites)
						# self.screen_manager.recenter(self.allsprites)
					elif event.key == pygame.K_r:
						self.screen_manager.reload()
					elif event.key == pygame.K_p:
						self.screen_manager.enlarge_screen(self.allsprites)
						# self.screen_manager.recenter(self.allsprites)
					elif event.key == pygame.K_o:
						self.screen_manager.shrink_screen(self.allsprites)
						# self.screen_manager.recenter(self.allsprites)
					elif event.key == pygame.K_l:
						self.screen_manager.show_info()
					elif event.key == pygame.K_j:
						self.joystick_manager.reload_joysticks()
					elif event.key == pygame.K_s:
						self.p1_joystick, self.p2_joystick = self.joystick_manager.select_joystick_configuration(self.screen_surf)
					elif event.key == pygame.K_y:
						print(self.p1_joystick, self.p2_joystick)
					elif event.key == pygame.K_m:
						pong_module.Pong(self).run()

				elif event.type == pygame.JOYBUTTONDOWN:
					virtual_joystick, button = self.joystick_manager.resolve_button_input(event.joy, event.button)
					if self.p1_joystick and self.p1_joystick == virtual_joystick:
						print('P1 using ' + virtual_joystick.name + ' -> ' + button)
					elif self.p2_joystick and self.p2_joystick == virtual_joystick:
						print('P2 using ' + virtual_joystick.name + ' -> ' + button)

				elif event.type == pygame.JOYHATMOTION:
					virtual_joystick, hat, side = self.joystick_manager.resolve_hat_input(event.joy, event.value)
					if self.p1_joystick and self.p1_joystick == virtual_joystick:
						s = 'P1 using ' + virtual_joystick.name + ' -> ' + hat
						if side:
							s += ', ' + side
						print(s)
					elif self.p2_joystick and self.p2_joystick == virtual_joystick:
						s = 'P2 using ' + virtual_joystick.name + ' -> ' + hat
						if side:
							s += ', ' + side
						print(s)

				for joystick in self.joystick_manager.joysticks:
					virtual_joystick, axes, sides = self.joystick_manager.resolve_axes(joystick)

					if self.p1_joystick and self.p1_joystick == virtual_joystick:
						for i in range(len(sides)):
							if axes[i]:
								print('P1 using ' + virtual_joystick.name + ' -> ' + axes[i] + ', ' + sides[i])

					if self.p2_joystick and self.p2_joystick == virtual_joystick:
						for i in range(len(sides)):
							if axes[i]:
								print('P2 using ' + virtual_joystick.name + ' -> ' + axes[i] + ', ' + sides[i])

			self.screen_surf.fill((0, 0, 0))
			self.screen_surf.blit(self.background_image, (0, 0))
			self.allsprites.update()
			self.allsprites.draw(self.screen_surf)
			pygame.display.flip()
			self.dt = self.clock.tick(Launcher.FPS)

	def quit(self):
		pygame.quit()
		sys.exit()


if __name__ == '__main__':
	pygame.init()
	Launcher().run()























	



























