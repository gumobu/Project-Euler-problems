from datetime import datetime
number = 0
sum_got = 0
start_time = datetime.now()
while number < 1000:
    if number % 5 == 0 or number % 3 == 0:  # Checking for multiplicity
        sum_got += number  # Increasing sum o the number, satisfied the condition
    number += 1  # Increasing number
print('sum is ', sum_got)
print(f'The program ran for {datetime.now() - start_time}')
