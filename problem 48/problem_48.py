from datetime import datetime

start_time = datetime.now()
sum_got = 0
for number in range(1, 1001):
    sum_got += (number ** number)
result = sum_got % 10000000000
print(f'The last ten digits are {result}')
print(f'The program ran for {datetime.now() - start_time}')
