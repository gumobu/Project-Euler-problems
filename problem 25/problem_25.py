count = 3
buf = 0
max_count = count
n1, n2 = 1, 1
n = n1 + n2
while len(str(n)) < 1000:
    buf = n
    n1, n2 = n2, buf
    n = n1 + n2
    count += 1

print(count)