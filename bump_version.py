#!/usr/bin/env python
import os
import sys

VERSION_FILE = 'VERSION.txt'

if os.path.isfile(VERSION_FILE):
    with open(VERSION_FILE) as f:
        version = list(map(int, f.read().split('.')))
else:
    version = [0, 0, 0]

if len(sys.argv) < 2:
    component = 'patch'
else:
    component = sys.argv[1]

if component == 'major':
    version[0] += 1
    version = [version[0] + 1, 0, 0]
elif component == 'minor':
    version = version[:2] + [0]
    version[1] += 1
elif component == 'patch':
    version[2] += 1

with open(VERSION_FILE, 'w') as f:
    f.write('{}.{}.{}'.format(*version))
