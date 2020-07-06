#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3




CONTROLS_MAP = {
				launcher_module.VirtualJoystick.SWITCH_PRO_CONTROLLER: {
					Pong.PLAYING_STATE: {
					   	launcher_module.VirtualJoystick.X: MOVE_UP,
						launcher_module.VirtualJoystick.B: MOVE_DOWN,

						launcher_module.VirtualJoystick.UP_ARROW: MOVE_UP_LOCKED,
						launcher_module.VirtualJoystick.DOWN_ARROW: MOVE_DOWN_LOCKED,
						launcher_module.VirtualJoystick.NEUTRAL_ARROW: STOP,

						launcher_module.VirtualJoystick.PLUS: PAUSE_TOGGLE_SIGNAL,
						launcher_module.VirtualJoystick.MINUS: PAUSE_TOGGLE_SIGNAL,
						launcher_module.VirtualJoystick.HOME: FULLSCREEN_TOGGLE_SIGNAL,
						launcher_module.VirtualJoystick.SNAPSHOT: FULLSCREEN_TOGGLE_SIGNAL,

						launcher_module.VirtualJoystick.BALL_UP: {
							launcher_module.VirtualJoystick.LEFT_SIDE_BALL: MOVE_UP,
							launcher_module.VirtualJoystick.RIGHT_SIDE_BALL: MOVE_UP
						},
						launcher_module.VirtualJoystick.BALL_DOWN: {
							launcher_module.VirtualJoystick.LEFT_SIDE_BALL: MOVE_DOWN,
							launcher_module.VirtualJoystick.RIGHT_SIDE_BALL: MOVE_DOWN
						},
						launcher_module.VirtualJoystick.BALL_NEUTRAL: {
							launcher_module.VirtualJoystick.LEFT_SIDE_BALL: STOP,
							launcher_module.VirtualJoystick.RIGHT_SIDE_BALL: STOP
						}
					}
				},

				launcher_module.VirtualJoystick.PAIRED_JOYCONS: {
					Pong.PLAYING_STATE: {
					   	launcher_module.VirtualJoystick.X: MOVE_UP,
						launcher_module.VirtualJoystick.B: MOVE_DOWN,

						launcher_module.VirtualJoystick.UP_ARROW: MOVE_UP,
						launcher_module.VirtualJoystick.DOWN_ARROW: MOVE_DOWN,

						launcher_module.VirtualJoystick.PLUS: PAUSE_TOGGLE_SIGNAL,
						launcher_module.VirtualJoystick.MINUS: PAUSE_TOGGLE_SIGNAL,

						launcher_module.VirtualJoystick.HOME: FULLSCREEN_TOGGLE_SIGNAL,
						launcher_module.VirtualJoystick.SNAPSHOT: FULLSCREEN_TOGGLE_SIGNAL,

						launcher_module.VirtualJoystick.BALL_UP: {
							launcher_module.VirtualJoystick.LEFT_SIDE_BALL: MOVE_UP_LOCKED,
							launcher_module.VirtualJoystick.RIGHT_SIDE_BALL: MOVE_UP_LOCKED
						},
						launcher_module.VirtualJoystick.BALL_UP_RIGHT: {
							launcher_module.VirtualJoystick.LEFT_SIDE_BALL: MOVE_UP_LOCKED,
							launcher_module.VirtualJoystick.RIGHT_SIDE_BALL: MOVE_UP_LOCKED
						},
						launcher_module.VirtualJoystick.BALL_UP_LEFT: {
							launcher_module.VirtualJoystick.LEFT_SIDE_BALL: MOVE_UP_LOCKED,
							launcher_module.VirtualJoystick.RIGHT_SIDE_BALL: MOVE_UP_LOCKED
						},
						launcher_module.VirtualJoystick.BALL_DOWN: {
							launcher_module.VirtualJoystick.LEFT_SIDE_BALL: MOVE_DOWN_LOCKED,
							launcher_module.VirtualJoystick.RIGHT_SIDE_BALL: MOVE_DOWN_LOCKED
						},
						launcher_module.VirtualJoystick.BALL_DOWN_RIGHT: {
							launcher_module.VirtualJoystick.LEFT_SIDE_BALL: MOVE_DOWN_LOCKED,
							launcher_module.VirtualJoystick.RIGHT_SIDE_BALL: MOVE_DOWN_LOCKED
						},
						launcher_module.VirtualJoystick.BALL_DOWN_LEFT: {
							launcher_module.VirtualJoystick.LEFT_SIDE_BALL: MOVE_DOWN_LOCKED,
							launcher_module.VirtualJoystick.RIGHT_SIDE_BALL: MOVE_DOWN_LOCKED
						},
						launcher_module.VirtualJoystick.BALL_NEUTRAL: {
							launcher_module.VirtualJoystick.LEFT_SIDE_BALL: STOP,
							launcher_module.VirtualJoystick.RIGHT_SIDE_BALL: STOP
						}
					}
				},


				launcher_module.VirtualJoystick.JOYCON_RIGHT_VERTICAL: {
					Pong.PLAYING_STATE: {
						launcher_module.VirtualJoystick.X: MOVE_UP,
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
					}
				},

				launcher_module.VirtualJoystick.JOYCON_LEFT_VERTICAL: {
					Pong.PLAYING_STATE: {
						launcher_module.VirtualJoystick.UP_ARROW: MOVE_UP,
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
				},

				launcher_module.VirtualJoystick.JOYCON_RIGHT_HORIZONTAL: {
					Pong.PLAYING_STATE: {
				   		launcher_module.VirtualJoystick.Y: MOVE_UP,
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
					}
				},

				launcher_module.VirtualJoystick.JOYCON_LEFT_HORIZONTAL: {
					Pong.PLAYING_STATE: {
						launcher_module.VirtualJoystick.UP_ARROW: MOVE_UP,
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
}


















# import pygame
# import pygame.freetype
# import sys
# pygame.init()

# sys.path.append('../')

# screen = pygame.display.set_mode((800, 600))
# # my_font = pygame.freetype.Font(None, 30)
# my_font = pygame.freetype.Font('fff_font.ttf', 30)
# fps = 80
# clock = pygame.time.Clock()

# while True:
# 	for event in pygame.event.get():
# 		if event.type == pygame.QUIT:
# 			pygame.quit()
# 			sys.exit()

# 	my_font.render_to(screen, (100, 100), 'hello world', (255, 0, 0))
# 	pygame.display.flip()
# 	dt = clock.tick(fps)
# 	# print(dt)
# 	actual_fps = 1000 / dt
# 	print(actual_fps)



# import random

# for i in range(10):
# 	print(random.randint(1, 5))
# 	print(random.random())

# import time

# s = time.time()
# print('s: ', s)
# while time.time() - s < 3:
# 	pass
# print('f: ', time.time())


# min_angle = 15
# max_angle = 45
# for i in range(10):
	# angles =   [random.randint(min_angle, max_angle), random.randint(180 - min_angle, 180 - max_angle), 
	# 			random.randint(-max_angle, - min_angle), random.randint(-180 + min_angle, -180 + max_angle)]
	# angles =   [random.randint(min_angle, max_angle), random.randint(180 - max_angle, 180 - min_angle),
	# 			random.randint(-max_angle, - min_angle), random.randint(-180 + min_angle, -180 + max_angle)]
	# a1 = random.randint(min_angle, max_angle)
	# print('a1', a1)
	# print('between', min_angle, max_angle)
	# a2 = random.randint(180 - max_angle, 180 - min_angle)
	# print('a2', a2)
	# print('between', 180 - max_angle, 180 - min_angle)
	# a3 = random.randint(-max_angle, - min_angle)
	# print('a3', a3)
	# print('between', -max_angle, -min_angle)
	# a4 = random.randint(-180 + min_angle, -180 + max_angle)
	# print('a4', a4)
	# print('between', -180 + min_angle, -180 + max_angle)
	# print(angles)






# a = [0, 1, 2, 3, 4, 5]
# a.append(6)
# b = a.pop(0)
# print(a)
# print(b)

# import pygame
# import sys

# pygame.init()

# screen = pygame.display.set_mode((800, 600))

# # print(pygame.display.list_modes())
# print(pygame.display.Info())

# while True:
# 	for event in pygame.event.get():
# 		if event.type == pygame.QUIT:
# 			pygame.quit()
# 			sys.exit()



# class Stick:
# 	def __init__(self, name, *physical_joysticks):
# 		self.name = name
# 		self.physical_joysticks = [physical_joystick for physical_joystick in physical_joysticks]

# 		print(self.physical_joysticks)

# Stick('ciao', 3)

# options = {0: 'ciao', 1: 'mamma', 2: 'guarda', 3: 'come', 4: 'mi', 5: 'diverto'}

# print('mamma' in options.values())

# a = [1, 2, 3]

# a.remove(2)
# print(a) # [1, 3]?

# print(options.keys())

# print((1-5)%3) # 2?


# del options[3]
# print(options)
# print(options.keys())
# print(options.values())
