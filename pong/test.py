#!/usr/local/opt/python@3.8/bin/python3

import os
import sys

sys.path.append('./dirtest')

import zest

print('this file: ', os.path.dirname(__file__))
print('sest module: ', os.path.dirname(zest.__file__))

zest.s()

# if __name__ == '__main__':
# 	pong.f()