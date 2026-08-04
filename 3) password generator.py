import random 

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"

count = int(input('Введите необходимое количество паролей для генерации'))
length = int(input('Введите длину пароля'))
is_digits = input('Включать ли цифры 0123456789? да/нет').lower()
is_upper = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? да/нет').lower()
is_lower = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? да/нет').lower()
is_symbol = input('Включать ли символы !#$%&*+-=?@^_? да/нет').lower()
is_strange = input('Исключать ли неоднозначные символы il1Lo0O? да/нет').lower()

chars = ''
if is_digits == 'да':
    chars += digits
if is_lower == 'да':
    chars += lowercase_letters
if is_upper == 'да':
    chars += uppercase_letters
if is_symbol == 'да':
    chars += punctuation
    
if not chars:
    print('Вы не выбрали ни одного типа символов. Используем цифры по умолчанию.')
    chars = digits


def generate_passwords(count, length, chars):
    passwords = []
    for _ in range(count):
        password = ''.join(random.choices(chars, k=length))
        passwords.append(password)
    return passwords

print(*generate_passwords(count, length, chars), sep='\n')