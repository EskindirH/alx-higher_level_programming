#!/usr/bin/python3
for r in range(122, 65, -1):
    if r == 96:
        break
    if r < 97 and r > 90:
        continue
    print('{:c}'.format(r if (r % 2 == 0) else (r - 32)), end='')
