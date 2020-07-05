#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import pygame
import pygame.freetype
import sys
import os
import random
import math
import time

sys.path.append('../')

import launcher_module


class Ball(pygame.sprite.Sprite):
	BALL_IMAGE = pygame.image.load(os.path.join(os.path.dirname(__file__), 'ball.png'))
	SPEED = 0.5

	def __init__(self, center_x, center_y, pong, *groups):
		pygame.sprite.Sprite.__init__(self, *groups)

		self.image = Ball.BALL_IMAGE
		self.rect = self.image.get_rect(center=(center_x, center_y))
		self.pong = pong
		self.min_x, self.max_x, self.min_y, self.max_y = pong.get_arena_borders()
		self.start_x, self.start_y = center_x, center_y

		self.speed = Ball.SPEED
		self.dx, self.dy = self.get_dx_dy(self.get_random_angle())

		self.frozen = True

	def freeze(self):
		self.frozen = True

	def unfreeze(self):
		self.frozen = False

	def reset(self):
		self.rect = self.image.get_rect(center=(self.start_x, self.start_y))
		self.speed = Ball.SPEED
		self.dx, self.dy = self.get_dx_dy(self.get_random_angle())
		self.start_time = time.time()

	def get_random_angle(self):
		min_angle = 15
		max_angle = 45
		angles =   [random.randint(min_angle, max_angle), random.randint(180 - max_angle, 180 - min_angle),
					random.randint(-max_angle, - min_angle), random.randint(-180 + min_angle, -180 + max_angle)]
		angle = random.choice(angles)

		return angle

	def get_dx_dy(self, angle):
		angle = math.radians(angle)
		dx = math.cos(angle)
		dy = -math.sin(angle)

		return dx, dy

	def move(self, dt):
		if not(self.dx or self.dy):
			return

		step_x = max(int(abs(self.dx) * self.speed * dt), 1)	
		step_y = max(int(abs(self.dy) * self.speed * dt), 1)

		self.rect.y += abs(self.dy) / self.dy * step_y
		self.bounce_off_horizontal_borders()
		self.bounce_off_pads(0, self.dy)

		self.rect.x += abs(self.dx) / self.dx * step_x
		self.bounce_off_pads(self.dx, 0)


	def bounce_off_horizontal_borders(self):
		if self.dy < 0 and self.rect.top < self.min_y:
			self.rect.top = self.min_y
			self.dy *= -1
		elif self.dy > 0 and self.rect.bottom > self.max_y:
			self.rect.bottom = self.max_y
			self.dy *= -1

	def score(self):
		if self.dx < 0 and self.rect.left < self.min_x:
			self.rect.left = self.min_x
			self.dx *= -1
			self.pong.update_score(Pong.P2)
			
		elif self.dx > 0 and self.rect.right > self.max_x:
			self.rect.right = self.max_x
			self.dx *= -1
			self.pong.update_score(Pong.P1)

	def increase_speed(self):
		self.speed += 0.03

	def bounce_off_pads(self, dx, dy):
		for pad in self.pong.allpads:
			if self.rect.colliderect(pad.rect):
				# Vertical bounce - move ball up and down until you find the closest free space
				if not dx:
					rect_up = self.rect.copy()
					rect_down = self.rect.copy()

					while rect_up.colliderect(pad.rect) and rect_down.colliderect(pad.rect):
						rect_up.y -= 1
						rect_down.y += 1

					if not rect_up.colliderect(pad.rect):
						self.rect = rect_up
					else:
						self.rect = rect_down
					self.dy *= -1

				# Horizontal bounce
				else:
					if dx > 0:
						self.rect.right = pad.rect.left
					else:
						self.rect.left = pad.rect.right
					self.dx *= -1
					self.increase_speed()

	def update(self, dt):
		if not self. frozen:
			self.move(dt)
			self.score()


class Pad(pygame.sprite.Sprite):
	# Commands
	PAD_IMAGE = pygame.image.load(os.path.join(os.path.dirname(__file__), 'pad.png'))
	MOVE_UP = 'MOVE_UP'
	MOVE_UP_LOCKED = 'MOVE_UP_LOCKED'
	MOVE_DOWN = 'MOVE_DOWN'
	MOVE_DOWN_LOCKED = 'MOVE_DOWN_LOCKED'
	STOP = 'STOP'

	# Signals
	PAUSE_TOGGLE_SIGNAL = 'PAUSE_TOGGLE_SIGNAL'
	FULLSCREEN_TOGGLE_SIGNAL = 'FULLSCREEN_TOGGLE_SIGNAL'

	CONTROLS_MAP = {launcher_module.VirtualJoystick.SWITCH_PRO_CONTROLLER:     {launcher_module.VirtualJoystick.X: MOVE_UP,
																				launcher_module.VirtualJoystick.B: MOVE_DOWN,

																				launcher_module.VirtualJoystick.UP_ARROW: MOVE_UP_LOCKED,
																				launcher_module.VirtualJoystick.DOWN_ARROW: MOVE_DOWN_LOCKED,
																				launcher_module.VirtualJoystick.NEUTRAL_ARROW: STOP,

																				launcher_module.VirtualJoystick.PLUS: PAUSE_TOGGLE_SIGNAL,
																				launcher_module.VirtualJoystick.MINUS: PAUSE_TOGGLE_SIGNAL,
																				launcher_module.VirtualJoystick.HOME: FULLSCREEN_TOGGLE_SIGNAL,
																				launcher_module.VirtualJoystick.SNAPSHOT: FULLSCREEN_TOGGLE_SIGNAL,

																				launcher_module.VirtualJoystick.BALL_UP:
																						{launcher_module.VirtualJoystick.LEFT_SIDE_BALL: MOVE_UP,
																						launcher_module.VirtualJoystick.RIGHT_SIDE_BALL: MOVE_UP
																						},
																				launcher_module.VirtualJoystick.BALL_DOWN:
																						{launcher_module.VirtualJoystick.LEFT_SIDE_BALL: MOVE_DOWN,
																						launcher_module.VirtualJoystick.RIGHT_SIDE_BALL: MOVE_DOWN
																						},
																				launcher_module.VirtualJoystick.BALL_NEUTRAL: 
																					   {launcher_module.VirtualJoystick.LEFT_SIDE_BALL: STOP,
																						launcher_module.VirtualJoystick.RIGHT_SIDE_BALL: STOP
																						}
																				},
					launcher_module.VirtualJoystick.PAIRED_JOYCONS:		  	   {launcher_module.VirtualJoystick.X: MOVE_UP,
																				launcher_module.VirtualJoystick.B: MOVE_DOWN,

																				launcher_module.VirtualJoystick.UP_ARROW: MOVE_UP,
																				launcher_module.VirtualJoystick.DOWN_ARROW: MOVE_DOWN,

																				launcher_module.VirtualJoystick.PLUS: PAUSE_TOGGLE_SIGNAL,
																				launcher_module.VirtualJoystick.MINUS: PAUSE_TOGGLE_SIGNAL,

																				launcher_module.VirtualJoystick.HOME: FULLSCREEN_TOGGLE_SIGNAL,
																				launcher_module.VirtualJoystick.SNAPSHOT: FULLSCREEN_TOGGLE_SIGNAL,

																				launcher_module.VirtualJoystick.BALL_UP: 
																					   {launcher_module.VirtualJoystick.LEFT_SIDE_BALL: MOVE_UP_LOCKED,
																						launcher_module.VirtualJoystick.RIGHT_SIDE_BALL: MOVE_UP_LOCKED
																						},
																				launcher_module.VirtualJoystick.BALL_UP_RIGHT: 
																					   {launcher_module.VirtualJoystick.LEFT_SIDE_BALL: MOVE_UP_LOCKED,
																						launcher_module.VirtualJoystick.RIGHT_SIDE_BALL: MOVE_UP_LOCKED
																						},
																				launcher_module.VirtualJoystick.BALL_UP_LEFT: 
																					   {launcher_module.VirtualJoystick.LEFT_SIDE_BALL: MOVE_UP_LOCKED,
																						launcher_module.VirtualJoystick.RIGHT_SIDE_BALL: MOVE_UP_LOCKED
																						},
																				launcher_module.VirtualJoystick.BALL_DOWN: 
																					   {launcher_module.VirtualJoystick.LEFT_SIDE_BALL: MOVE_DOWN_LOCKED,
																						launcher_module.VirtualJoystick.RIGHT_SIDE_BALL: MOVE_DOWN_LOCKED
																						},
																				launcher_module.VirtualJoystick.BALL_DOWN_RIGHT: 
																					   {launcher_module.VirtualJoystick.LEFT_SIDE_BALL: MOVE_DOWN_LOCKED,
																						launcher_module.VirtualJoystick.RIGHT_SIDE_BALL: MOVE_DOWN_LOCKED
																						},
																				launcher_module.VirtualJoystick.BALL_DOWN_LEFT: 
																					   {launcher_module.VirtualJoystick.LEFT_SIDE_BALL: MOVE_DOWN_LOCKED,
																						launcher_module.VirtualJoystick.RIGHT_SIDE_BALL: MOVE_DOWN_LOCKED
																						},
																				launcher_module.VirtualJoystick.BALL_NEUTRAL: 
																					   {launcher_module.VirtualJoystick.LEFT_SIDE_BALL: STOP,
																						launcher_module.VirtualJoystick.RIGHT_SIDE_BALL: STOP
																						}
																			   },
					launcher_module.VirtualJoystick.JOYCON_RIGHT_VERTICAL:     {launcher_module.VirtualJoystick.X: MOVE_UP,
																				launcher_module.VirtualJoystick.B: MOVE_DOWN,

																				launcher_module.VirtualJoystick.PLUS: PAUSE_TOGGLE_SIGNAL,
																				launcher_module.VirtualJoystick.HOME: FULLSCREEN_TOGGLE_SIGNAL,

																				launcher_module.VirtualJoystick.BALL_UP: MOVE_UP_LOCKED,
																				launcher_module.VirtualJoystick.BALL_UP_RIGHT: MOVE_UP_LOCKED,
																				launcher_module.VirtualJoystick.BALL_UP_LEFT: MOVE_UP_LOCKED,
																				launcher_module.VirtualJoystick.BALL_DOWN: MOVE_DOWN_LOCKED,
																				launcher_module.VirtualJoystick.BALL_DOWN_RIGHT: MOVE_DOWN_LOCKED,
																				launcher_module.VirtualJoystick.BALL_DOWN_LEFT: MOVE_DOWN_LOCKED,
																				launcher_module.VirtualJoystick.BALL_NEUTRAL: STOP
																				},
					launcher_module.VirtualJoystick.JOYCON_LEFT_VERTICAL:	   {launcher_module.VirtualJoystick.UP_ARROW: MOVE_UP,
																				launcher_module.VirtualJoystick.DOWN_ARROW: MOVE_DOWN,

																				launcher_module.VirtualJoystick.MINUS: PAUSE_TOGGLE_SIGNAL,
																				launcher_module.VirtualJoystick.SNAPSHOT: FULLSCREEN_TOGGLE_SIGNAL,

																				launcher_module.VirtualJoystick.BALL_UP: MOVE_UP_LOCKED,
																				launcher_module.VirtualJoystick.BALL_UP_RIGHT: MOVE_UP_LOCKED,
																				launcher_module.VirtualJoystick.BALL_UP_LEFT: MOVE_UP_LOCKED,
																				launcher_module.VirtualJoystick.BALL_DOWN: MOVE_DOWN_LOCKED,
																				launcher_module.VirtualJoystick.BALL_DOWN_RIGHT: MOVE_DOWN_LOCKED,
																				launcher_module.VirtualJoystick.BALL_DOWN_LEFT: MOVE_DOWN_LOCKED,
																				launcher_module.VirtualJoystick.BALL_NEUTRAL: STOP
																				},
					launcher_module.VirtualJoystick.JOYCON_RIGHT_HORIZONTAL:   {launcher_module.VirtualJoystick.Y: MOVE_UP,
																				launcher_module.VirtualJoystick.A: MOVE_DOWN,

																				launcher_module.VirtualJoystick.PLUS: PAUSE_TOGGLE_SIGNAL,
																				launcher_module.VirtualJoystick.HOME: FULLSCREEN_TOGGLE_SIGNAL,

																				launcher_module.VirtualJoystick.BALL_UP: MOVE_UP_LOCKED,
																				launcher_module.VirtualJoystick.BALL_UP_RIGHT: MOVE_UP_LOCKED,
																				launcher_module.VirtualJoystick.BALL_UP_LEFT: MOVE_UP_LOCKED,
																				launcher_module.VirtualJoystick.BALL_DOWN: MOVE_DOWN_LOCKED,
																				launcher_module.VirtualJoystick.BALL_DOWN_RIGHT: MOVE_DOWN_LOCKED,
																				launcher_module.VirtualJoystick.BALL_DOWN_LEFT: MOVE_DOWN_LOCKED,
																				launcher_module.VirtualJoystick.BALL_NEUTRAL: STOP
																				},
					launcher_module.VirtualJoystick.JOYCON_LEFT_HORIZONTAL:	   {launcher_module.VirtualJoystick.UP_ARROW: MOVE_UP,
																				launcher_module.VirtualJoystick.DOWN_ARROW: MOVE_DOWN,

																				launcher_module.VirtualJoystick.MINUS: PAUSE_TOGGLE_SIGNAL,
																				launcher_module.VirtualJoystick.SNAPSHOT: FULLSCREEN_TOGGLE_SIGNAL,

																				launcher_module.VirtualJoystick.BALL_UP: MOVE_UP_LOCKED,
																				launcher_module.VirtualJoystick.BALL_UP_RIGHT: MOVE_UP_LOCKED,
																				launcher_module.VirtualJoystick.BALL_UP_LEFT: MOVE_UP_LOCKED,
																				launcher_module.VirtualJoystick.BALL_DOWN: MOVE_DOWN_LOCKED,
																				launcher_module.VirtualJoystick.BALL_DOWN_RIGHT: MOVE_DOWN_LOCKED,
																				launcher_module.VirtualJoystick.BALL_DOWN_LEFT: MOVE_DOWN_LOCKED,
																				launcher_module.VirtualJoystick.BALL_NEUTRAL: STOP
																				}
	}

	SPEED = 0.5
	DISTANCE_FROM_ARENA_BORDER = 50

	

	def __init__(self, side, joystick, x, y, pong, *groups):
		pygame.sprite.Sprite.__init__(self, *groups)
		self.image = Pad.PAD_IMAGE
		self.rect = self.image.get_rect(midleft=(x, y))
		self.side = side
		self.virtual_joystick = joystick
		self.pong = pong
		self.start_x, self.start_y = x, y
		self.min_x, self.max_x, self.min_y, self.max_y = self.pong.get_arena_borders()

		self.score = 0

		self.command_queue = []
		self.dy = 0
		self.speed = Pad.SPEED
		self.locked = False
		self.signal = None
		self.frozen = True

	def freeze(self):
		self.frozen = True

	def unfreeze(self):
		self.frozen = False

	def reset(self):
		self.rect = self.image.get_rect(midleft=(self.start_x, self.start_y))
		self.command_queue = []
		self.dy = 0
		self.speed = Pad.SPEED
		self.locked = False
		self.start_time = time.time()

	def process_joystick_button_input(self, button):
		try:
			control = Pad.CONTROLS_MAP[self.virtual_joystick.name][button]
			self.command_queue.append(control)
			# print(self.side + ' received: ' + control)
		except:
			pass
			# print('no map for ', button)

	def process_joystick_hat_input(self, hat, ball_side):
		control = None
		try:
			# Paired joycons - physical hats = balls, they have a side
			control = Pad.CONTROLS_MAP[self.virtual_joystick.name][hat][ball_side]
			self.command_queue.append(control)
			# print(self.side + ' received: ' + control)
		except:
			pass

		try:
			if not control:
				# Pro controller - physical hats = arrows, no side
				control = Pad.CONTROLS_MAP[self.virtual_joystick.name][hat]
				self.command_queue.append(control)
				# print(self.side + ' received: ' + control)
		except:
			pass
			# print('no map for ', hat, ball_side)

	def process_joystick_axes_input(self, axes, sides):
		for i in range(len(sides)):
			try:
				control = Pad.CONTROLS_MAP[self.virtual_joystick.name][axes[i]][sides[i]]
				self.command_queue.append(control)
				# print(self.side + ' received: ' + control)
			except:
				pass
				# print('no map for ', axes, sides)

	def process_movement_command(self, command, dt):
		if command in (Pad.MOVE_UP, Pad.MOVE_UP_LOCKED):
			self.dy = -1
		elif command in (Pad.MOVE_DOWN, Pad.MOVE_DOWN_LOCKED):
			self.dy = 1

		if command in (Pad.MOVE_UP_LOCKED, Pad.MOVE_DOWN_LOCKED):
			self.locked = True

	def check_ball_collision(self):
		if self.rect.colliderect(self.pong.ball.rect):
			min_top = self.min_y + self.pong.ball.rect.height
			max_bottom = self.max_y - self.pong.ball.rect.height

			if self.rect.top < min_top:
				self.rect.top = min_top
			elif self.rect.bottom > max_bottom:
				self.rect.bottom = max_bottom

	def check_wall_collision(self):
		if self.dy < 0 and self.rect.top < self.min_y:
			self.rect.top = self.min_y
		elif self.dy > 0 and self.rect.bottom > self.max_y:
			self.rect.bottom = self.max_y

	def move(self, dt):
		if not self.dy:
			return

		step_y = max(int(abs(self.dy) * self.speed * dt), 1)
		self.rect.y += abs(self.dy) / self.dy * step_y

		self.check_ball_collision()
		self.check_wall_collision()

		if not self.locked:
			self.dy = 0

	def stop(self):
		self.locked = False
		self.dy = 0

	def update(self, dt):
		self.signal = None

		while self.command_queue:
			command = self.command_queue.pop(0)
			if command in (Pad.MOVE_UP, Pad.MOVE_DOWN, Pad.MOVE_UP_LOCKED, Pad.MOVE_DOWN_LOCKED):
				if not self.frozen:
					self.process_movement_command(command, dt)
			elif command == Pad.STOP:
				if not self.frozen:
					self.stop()
			elif command in (Pad.PAUSE_TOGGLE_SIGNAL, Pad.FULLSCREEN_TOGGLE_SIGNAL):
				self.signal = command

		self.move(dt)
			

class Pong:
	BACKGROUND_IMAGE = pygame.image.load(os.path.join(os.path.dirname(__file__), 'pong_background.png'))
	P1 = 'P1'
	P2 = 'P2'

	PRE_START_TIME = 1.5

	PRE_START_STATE = 'PRE_START_STATE'
	PLAYING_STATE = 'PLAYING_STATE'
	PAUSED_STATE = 'PAUSED_STATE'

	FONT_COLOR = (48, 80, 65)
	FONT_SIZE = 100
	FONT_NAME = 'fff_font.ttf'

	def __init__(self, launcher):
		self.launcher = launcher

		self.background_image = Pong.BACKGROUND_IMAGE
		self.screen_surf = self.launcher.screen_surf

		self.p1_joystick, self.p2_joystick = self.launcher.p1_joystick, self.launcher.p2_joystick

		self.allsprites = pygame.sprite.Group()
		self.allpads = pygame.sprite.Group()
		self.allballs = pygame.sprite.Group()

		self.p1_pad, self.p2_pad = None, None
		self.create_pads()
		self.ball = None 
		self.create_ball()

		self.state = Pong.PRE_START_STATE
		self.pre_start_state_time = time.time()

		self.my_font = pygame.freetype.Font(Pong.FONT_NAME, Pong.FONT_SIZE)

		self.clock = self.launcher.clock
		self.dt = self.launcher.dt
		self.fps = launcher_module.Launcher.FPS


	def set_state(self, state):
		self.state = state

		if state == Pong.PRE_START_STATE:
			self.pre_start_state_time = time.time()
			for pad in self.allpads:
				pad.freeze()
			self.ball.freeze()

		elif state == Pong.PLAYING_STATE:
			for pad in self.allpads:
				pad.unfreeze()
			self.ball.unfreeze()

		elif state == Pong.PAUSED_STATE:
			for pad in self.allpads:
				pad.stop()
				pad.freeze()
			self.ball.freeze()

	def draw_pause(self):
		pause_string = 'PAUSED'

		pause_surf, pause_rect = self.my_font.render(pause_string, Pong.FONT_COLOR)
		pause_rect.centerx, pause_rect.centery = self.screen_surf.get_width() // 2, self.screen_surf.get_height() // 2

		self.screen_surf.blit(pause_surf, pause_rect)


	def draw_score(self):
		p1_score_surf, p1_score_rect = self.my_font.render(str(self.p1_pad.score), Pong.FONT_COLOR)
		p2_score_surf, p2_score_rect = self.my_font.render(str(self.p2_pad.score), Pong.FONT_COLOR)

		p1_score_rect.right = self.screen_surf.get_width() // 2 - 100
		p2_score_rect.left = self.screen_surf.get_width() // 2 + 100

		self.screen_surf.blit(p1_score_surf, p1_score_rect)
		self.screen_surf.blit(p2_score_surf, p2_score_rect)


	def update_score(self, side):
		for pad in self.allpads:
			if pad.side == side:
				pad.score += 1

		self.reset_pads_and_ball()
		self.set_state(Pong.PRE_START_STATE)


	def reset_pads_and_ball(self):
		for sprite in (self.ball, self.p1_pad, self.p2_pad):
			sprite.reset()


	def create_pads(self):
		left_1 = self.get_arena_borders()[0] + Pad.DISTANCE_FROM_ARENA_BORDER
		left_2 = self.get_arena_borders()[1] - Pad.DISTANCE_FROM_ARENA_BORDER - Pad.PAD_IMAGE.get_rect().width
		center_y = self.get_arena_borders()[3] // 2

		pad_1 = Pad(Pong.P1, self.p1_joystick, left_1, center_y, self, self.allpads, self.allsprites)
		pad_2 = Pad(Pong.P2, self.p2_joystick, left_2, center_y, self, self.allpads, self.allsprites)

		self.p1_pad, self.p2_pad = pad_1, pad_2
		# return pad_1, pad_2

	def create_ball(self):
		center_x = self.get_arena_borders()[1] // 2
		center_y = self.get_arena_borders()[3] // 2
		self.ball = Ball(center_x, center_y, self, self.allballs, self.allsprites)
		# return Ball(center_x, center_y, self, self.allballs, self.allsprites)

	def get_arena_borders(self):
		# Customizable in the future
		min_x = 0
		max_x = self.screen_surf.get_width()
		min_y = 0
		max_y = self.screen_surf.get_height()

		return min_x, max_x, min_y, max_y		

	def toggle_fullscreen(self):
		self.launcher.screen_manager.toggle_fullscreen()

	def quit(self):
		pygame.quit()
		sys.exit()

	def process_keyboard_input(self, key):
		if key == pygame.K_ESCAPE:
			self.quit()

		elif key == pygame.K_w:
			self.toggle_fullscreen()
		
		if self.state == Pong.PLAYING_STATE:
			if key == pygame.K_SPACE:
				self.set_state(Pong.PAUSED_STATE)

		elif self.state == Pong.PAUSED_STATE:
			if key == pygame.K_SPACE:
				self.set_state(Pong.PLAYING_STATE)

		

	def process_joystick_button_input(self, event):
		virtual_joystick, button = self.launcher.joystick_manager.resolve_button_input(event.joy, event.button)

		if self.p1_joystick and self.p1_joystick == virtual_joystick:
			self.p1_pad.process_joystick_button_input(button)
		elif self.p2_joystick and self.p2_joystick == virtual_joystick:
			self.p2_pad.process_joystick_button_input(button)

	def process_joystick_hat_input(self, event):
		virtual_joystick, hat, ball_side = self.launcher.joystick_manager.resolve_hat_input(event.joy, event.value)

		if self.p1_joystick and self.p1_joystick == virtual_joystick:
			self.p1_pad.process_joystick_hat_input(hat, ball_side)
		elif self.p2_joystick and self.p2_joystick == virtual_joystick:
			self.p2_pad.process_joystick_hat_input(hat, ball_side)
			
	def process_joystick_axes_input(self):
		for physical_joystick in self.launcher.joystick_manager.joysticks:
			virtual_joystick, axes, sides = self.launcher.joystick_manager.resolve_axes(physical_joystick)

			if self.p1_joystick and self.p1_joystick == virtual_joystick:
				self.p1_pad.process_joystick_axes_input(axes, sides)
			elif self.p2_joystick and self.p2_joystick == virtual_joystick:
				self.p2_pad.process_joystick_axes_input(axes, sides)

	def update_state(self):
		if self.state == Pong.PRE_START_STATE:
			if time.time() - self.pre_start_state_time > Pong.PRE_START_TIME:
				self.set_state(Pong.PLAYING_STATE)

	def check_signals(self):
		for pad in self.allpads:
			if pad.signal == Pad.PAUSE_TOGGLE_SIGNAL:
				if self.state == Pong.PLAYING_STATE:
					self.set_state(Pong.PAUSED_STATE)
				elif self.state == Pong.PAUSED_STATE:
					self.set_state(Pong.PLAYING_STATE)
			if pad.signal == Pad.FULLSCREEN_TOGGLE_SIGNAL:
				self.toggle_fullscreen()


	def update(self):
		self.update_state()
		self.allpads.update(self.dt)
		self.allballs.update(self.dt)
		self.check_signals()

	def draw(self):
		self.screen_surf.fill((0, 0, 0))
		self.screen_surf.blit(self.background_image, (0, 0))
		self.allsprites.draw(self.screen_surf)

		if self.state == Pong.PRE_START_STATE:
			self.draw_score()

		elif self.state == Pong.PAUSED_STATE:
			self.draw_pause()

		pygame.display.flip()


	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.quit()

				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_p:
						return
					self.process_keyboard_input(event.key)

				elif event.type == pygame.JOYBUTTONDOWN:
					self.process_joystick_button_input(event)

				elif event.type == pygame.JOYHATMOTION:
					self.process_joystick_hat_input(event)

			self.process_joystick_axes_input()

			self.update()
			self.draw()
			self.dt = self.clock.tick(self.fps)



if __name__ == '__main__':
	pass



















