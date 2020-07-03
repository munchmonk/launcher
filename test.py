#!/usr/local/opt/python@3.8/bin/python3

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

options = {0: 'ciao', 1: 'mamma', 2: 'guarda', 3: 'come', 4: 'mi', 5: 'diverto'}
del options[3]
print(options)
print(options.keys())
print(options.values())
