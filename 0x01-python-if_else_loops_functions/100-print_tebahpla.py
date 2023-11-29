#!/usr/bin/python3
for r in range(122, 65, -2):
    if r == 96:
        break
    if r < 97 and r > 90:
        continue
    print(f'{r:c}{r - 33:c}', end='')
