#!/usr/local/opt/python@3.8/bin/python3

import random

# for i in range(10):
# 	print(random.randint(1, 5))
# 	print(random.random())


min_angle = 15
max_angle = 45
for i in range(10):
	# angles =   [random.randint(min_angle, max_angle), random.randint(180 - min_angle, 180 - max_angle), 
	# 			random.randint(-max_angle, - min_angle), random.randint(-180 + min_angle, -180 + max_angle)]
	angles =   [random.randint(min_angle, max_angle), random.randint(180 - max_angle, 180 - min_angle),
				random.randint(-max_angle, - min_angle), random.randint(-180 + min_angle, -180 + max_angle)]
	a1 = random.randint(min_angle, max_angle)
	print('a1', a1)
	print('between', min_angle, max_angle)
	a2 = random.randint(180 - max_angle, 180 - min_angle)
	print('a2', a2)
	print('between', 180 - max_angle, 180 - min_angle)
	a3 = random.randint(-max_angle, - min_angle)
	print('a3', a3)
	print('between', -max_angle, -min_angle)
	a4 = random.randint(-180 + min_angle, -180 + max_angle)
	print('a4', a4)
	print('between', -180 + min_angle, -180 + max_angle)
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
