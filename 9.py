m = 0
while True:
	n = int(input())
	if n > m:
		m = n
	if n == 0:
		break
print(m)