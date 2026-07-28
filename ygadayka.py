from random import randint

random_number = randint(1, 100)

print('Добро пожаловать в числовую угадайку')

def is_valid(text):
    if text.isdigit():          # проверяем, что введены только цифры
        number = int(text)
        return 1 <= number <= 100
    return False

def ask_number():
    while True:
        user_input = input('Введите число от 1 до 100: ')
        if is_valid(user_input):
            return int(user_input)
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')

# Основной игровой цикл
while True:
    number = ask_number()        # получаем корректное число
    if number < random_number:
        print('Ваше число меньше загаданного, попробуйте еще разок')
    elif number > random_number:
        print('Ваше число больше загаданного, попробуйте еще разок')
    else:
        print('Вы угадали, поздравляем!')
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
        break
print('Change2')