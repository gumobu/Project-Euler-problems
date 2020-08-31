from datetime import datetime
sum_of_squares, sum_of_n = 0, 0
n = 100
start_time = datetime.now()
for number in range(n + 1):
    sum_of_squares += (number ** 2)
    sum_of_n += number
print(f'the difference between the sum of the squares and the square of the sum '
      f'is {(sum_of_n ** 2) - sum_of_squares}')
print(f'The program ran for {datetime.now() - start_time}')
