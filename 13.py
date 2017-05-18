n = int(input())
m = int(input())

while m > 0 and n > 0:
    if m > n:
        m = m - n
    else:
        n = n - m
 
print(m)