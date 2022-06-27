import random

random_number = random.randint(1, 3)
user_number = input('Угадай число от 1 до 3: ')

if int(user_number) == random_number:
    print('Ты угадал :)')
    print(f'Было загадано число: {random_number} ')
else:
    print('Ты не угадал :(')
    print(f'Было загадано число: {random_number} ')

