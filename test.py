#!/usr/local/opt/python@3.8/bin/python3

import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))

# print(pygame.display.list_modes())
print(pygame.display.Info())

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()