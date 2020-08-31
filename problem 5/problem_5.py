from datetime import datetime
number = 20  # Minimal number dividable on 20
divider = 19  # Minimal divider necessary to check dividable on.
start_time = datetime.now()
while divider > 0:
    if number % divider == 0:  # Checking for full divisibility on divider
        divider -= 1
    else:
        number += 20
        divider = 19
    if divider == 1:
        print(f'The number is {number}')
        break
print(f'The program ran for {datetime.now() - start_time}')
