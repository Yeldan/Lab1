import math
a = float(input())
b = float(input())
c = float(input())

d = b * b - 4 * a * c
if d == 0:
	print(-b / 2.0 * a)
if d > 0:
	print((-b - math.sqrt(d)) / 2.0 * a)
	print((-b + math.sqrt(d)) / 2.0 * a)