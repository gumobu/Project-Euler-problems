from datetime import datetime
sum_got = 0
start_time = datetime.now()
for symbol in str(2 ** 1000):
    sum_got += int(symbol)
print(f'sum is {sum_got}')
print(f'The program ran for {datetime.now() - start_time}')
