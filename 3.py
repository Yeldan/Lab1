a = input()
b = input()
if a == 0 and b == 0:
	print("INF")
if a == 0 and b != 0:
	print("NO")
if a != 0 and b == 0:
	print('0')
if b % a == 0:
		print(-b // a)
else:
			print("NO")
