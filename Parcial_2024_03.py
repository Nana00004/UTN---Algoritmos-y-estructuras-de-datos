import random

random.seed(4142)
n1 = 19000
n2 = 50

c1 = c2 = c3 = pn = cant = 0

for i in range(n1):
    num: int = random.randint(-27000, 13000)
    # Punto 1...
    if -13000 > num >= -27000:
        c1 += 1
    elif num > -13000:
        c2 += 1
    if num > 0:
        pass
    # Punto 2...

    # Punto 3...
    if num > 1500 and (num % 3 == 0 or num % 7 == 0):
        cant += num
        c3 += 1

prom = int(cant / c3)
# Punto 4...

p1 = int(c3 * 100 / n2)

print(c1, c2, prom, p1)
