import random

# генерируем случайное число от 1 до 10
number = random.randint(1, 10)

# запрашиваем у пользователя угадать число
guess = int(input("Угадайте число от 1 до 10: "))

# проверяем, правильно ли угадал пользователь
if guess == number:
    print("Вы угадали число!")
else:
    print("Неправильно. Загаданное число было", number)