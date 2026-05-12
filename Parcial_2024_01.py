# Turno 01
import random

random.seed(2759)

c1 = c2 = c3 = p = c4 = c5 = c6 = 0
anterior = 0

for i in range(15000):
    num = random.randint(1, 53000)
    if 17000 > num >= 1:
        c1 += 1
    if 17000 <= num < 37000:
        c2 += 1
    if num >= 37000:
        c3 += 1
    if num >= 25000 and num % 4 == 0:
        c5 += num
        c4 += 1
    if num % 3 == 0:
        if num > anterior:
            anterior = num
    if num % 5 == 0:
        c6 += 1

p2 = int((c6 * 100) / 15000)
p = int(c5 / c4)
print("Numeros mayores o iguales a 1 pero menores a 17000: ", c1)
print("Numeros mayores o iguales a 17000 y menores a 37000: ", c2)
print("Numeros mayores o iguales a 37000: ", c3)
print("El promedio de los numeros mayores o iguales a 25000 y divisibles por 4 es: ", p)
print("El mayor entre los numeros divisibles por 3 es: ", anterior)
print("El porcentaje de numeros divisibles por 5 es: ", p2)


