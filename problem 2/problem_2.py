from datetime import datetime
sum_got, number_previous, number_current, buf = 0, 1, 1, 0  # Let the Fibonnaci line start with '1 1'
start_time = datetime.now()
while True:
    buf = number_current  # Using a buffer variable to change values of number_previous and number_current
    number_current = number_current + number_previous  # Getting a new number_current value as a result of addition
    number_previous = buf  # Setting the value of number_previous equal to buffer variable
    if number_current % 2 == 0:
        print(number_current)
        if number_current < 4000000:
            sum_got += number_current
        else:
            break
print(f'sum is {sum_got}')
print(f'The program ran for {datetime.now() - start_time}')
