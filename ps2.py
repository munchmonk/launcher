
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

	

PS2_NAME = 'Twin USB Joystick'
PS2_JOYSTICK_LEFT, PS2_JOYSTICK_RIGHT, SWITCH_PRO_CONTROLLER, JOYCON_LEFT, JOYCON_RIGHT, PAIRED_JOYCONS = range(6)

(CROSS, SQUARE, TRIANGLE, CIRCLE, 
	START, SELECT,
	R1, R2, R3, L1, L2, L3) = range(12)

PS2_HATS_MAP = 	   {0: PS2_JOYSTICK_RIGHT,
						1: PS2_JOYSTICK_LEFT
	}	

	PS2_BUTTONS_MAP =  {0:  (PS2_JOYSTICK_RIGHT, TRIANGLE),
						1:  (PS2_JOYSTICK_RIGHT, CIRCLE),
						2:  (PS2_JOYSTICK_RIGHT, CROSS),
						3:  (PS2_JOYSTICK_RIGHT, SQUARE),
						4:  (PS2_JOYSTICK_RIGHT, L2),
						5:  (PS2_JOYSTICK_RIGHT, R2),
						6:  (PS2_JOYSTICK_RIGHT, L1),
						7:  (PS2_JOYSTICK_RIGHT, R1),
						8:  (PS2_JOYSTICK_RIGHT, SELECT),
						9:  (PS2_JOYSTICK_RIGHT, START),
						10: (PS2_JOYSTICK_RIGHT, L3),
						11: (PS2_JOYSTICK_RIGHT, R3),
						12: (PS2_JOYSTICK_LEFT, TRIANGLE),
						13: (PS2_JOYSTICK_LEFT, CIRCLE),
						14: (PS2_JOYSTICK_LEFT, CROSS),
						15: (PS2_JOYSTICK_LEFT, SQUARE),
						16: (PS2_JOYSTICK_LEFT, L2),
						17: (PS2_JOYSTICK_LEFT, R2),
						18: (PS2_JOYSTICK_LEFT, L1),
						19: (PS2_JOYSTICK_LEFT, R1),
						20: (PS2_JOYSTICK_LEFT, SELECT),
						21: (PS2_JOYSTICK_LEFT, START),
						22: (PS2_JOYSTICK_LEFT, L3),
						23: (PS2_JOYSTICK_LEFT, R3)
	}

# if self._identify(joystick_id) == JoystickManager.PS2_NAME:
		# 	joystick, button = JoystickManager.PS2_BUTTONS_MAP[button_id][0], JoystickManager.PS2_BUTTONS_MAP[button_id][1]


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

					# if joystick == self.joystick_manager.PS2_JOYSTICK_LEFT:
					# 	if arrow == self.joystick_manager.UP_ARROW:
					# 		print('P1, jump!')
					# elif joystick == self.joystick_manager.PS2_JOYSTICK_RIGHT:
					# 	if arrow == self.joystick_manager.UP_ARROW:
					# 		print('P2, jump!')