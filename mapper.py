#!/usr/bin/env python
import sys
import re

for line in sys.stdin:
    line = line.strip()
    words = re.findall(r'\w+', line.lower())
    for word in words:
        print(f'{word}\t1')
