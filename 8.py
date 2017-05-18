n = int(input())
l = range(1,n + 1)
sum = 1.0
sign = -1
for i in l:
		sum += sign / (2.0 * i + 1)
		sign = -sign

print(float(4 * sum))
