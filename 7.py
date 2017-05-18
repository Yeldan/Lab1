n = int(input())
l = range(1,n +1)
sum = 0
for i in l:
	sum += float(1.0 / (i * i))
print(sum)