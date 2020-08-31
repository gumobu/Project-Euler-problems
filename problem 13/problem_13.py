from datetime import datetime
sum_got = 0
start_time = datetime.now()
file = open('numbers.txt', 'r')
list_to_sum = file.read().split('\n')
file.close()
for element in list_to_sum:
    sum_got += int(element)
final_line = str(sum_got)[0:10]
print(final_line)
print(f'The program ran for {datetime.now() - start_time}')
