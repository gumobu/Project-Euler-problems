from  datetime import datetime
max_palindrome = 0
start_time = datetime.now()
for number_1 in range(100, 1000):
    for number_2 in range(100, 1000):  # Loops for finding compositions
        composition = number_1 * number_2
        str_composition = str(composition)
        _ = 0
        while _ < (len(str_composition) // 2):  # Checks the equality of two symbols, moving from sides to center
            if str_composition[0 + _] != str_composition[len(str_composition) - 1 - _]:
                break
            else:
                _ += 1
                if _ == len(str_composition) // 2:
                    if composition > max_palindrome:
                        max_palindrome = composition
                    break
print(f'The largest palindrome made from the product of two 3-digit numbers is {max_palindrome}')
print(f'The program ran for {datetime.now() - start_time}')
