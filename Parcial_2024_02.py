# Turno 04

import random
random.seed(1475)
sn = c1 = c2 = c3 = cant = m = p = p2 = 0

for i in range(50):
    num = random.randint(-100, 15000)
    if num < 0:
        sn += num
    if 0 <= num < 10000 and num % 4 == 0:
        c1 += 1
    if num > 10000:
        c2 += 1
    if 0 < num <= 8000 and num % 6 == 0:
        c3 += 1
        cant += num
    if num > 5000 and num % 5 == 0:
        if num > m:
            m = num
    if num % 2 == 0:
        p2 += 1

p2 = int(p2 * 100 / 50)
p = int(cant / c3)
print(sn)
print(c1)
print(c2)
print(p)
print(m)
print(p2)