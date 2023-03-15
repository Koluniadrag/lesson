import random

input_string = input("Введите строку: ")
num_strings = 5

for i in range(num_strings):
    random_string = ''.join(random.choice(input_string) for _ in range(len(input_string)))
    print(random_string)