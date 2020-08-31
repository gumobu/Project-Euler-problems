max_sum, sum_current = 0, 0
for a in range(100):
    for b in range(100):
        for number in str(a ** b):
            sum_current += int(number)
        if sum_current > max_sum:
            max_sum = sum_current
        sum_current = 0
print(max_sum)
