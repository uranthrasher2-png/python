from random import randint

print('Добро пожаловать в числовую угадайку!')

def get_positive_int(prompt):
    while True:
        value = input(prompt)
        if value.isdigit() and int(value) >= 1:
            return int(value)
        print('Нужно ввести целое положительное число!')

def is_valid(text, max_val):
    if text.isdigit():
        number = int(text)
        return 1 <= number <= max_val
    return False

def ask_number(max_val):
    while True:
        user_input = input(f'Введите число от 1 до {max_val}: ')
        if is_valid(user_input, max_val):
            return int(user_input)
        print(f'А может быть все-таки введем целое число от 1 до {max_val}?')

# Основной цикл для повторных игр
while True:
    max_number = get_positive_int('Введите правую границу для загаданного числа (от 1 до n): ')
    if max_number < 2:
        print('Граница должна быть не менее 2, чтобы игра имела смысл.')
        continue

    random_number = randint(1, max_number)
    attempts = 0

    print(f'Я загадал число от 1 до {max_number}. Попробуйте угадать!')

    while True:
        number = ask_number(max_number)
        attempts += 1

        if number < random_number:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif number > random_number:
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            print('Вы угадали, поздравляем!')
            print(f'Количество попыток: {attempts}')
            break

    answer = input('Если хотите сыграть еще, введите "да": ').strip().lower()
    if answer != 'да':
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
        break