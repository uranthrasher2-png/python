from random import randint

print('Добро пожаловать в числовую угадайку')

def is_valid(text):
    if text.isdigit():
        number = int(text)
        return 1 <= number <= 100
    return False

def ask_number():
    while True:
        user_input = input('Введите число от 1 до 100: ')
        if is_valid(user_input):
            return int(user_input)
        print('А может быть все-таки введем целое число от 1 до 100?')

while True:
    random_number = randint(1, 100)
    attempts = 0

    while True:
        number = ask_number()
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