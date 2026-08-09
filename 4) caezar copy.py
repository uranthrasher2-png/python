purpose = input('Введите в поле - ш (шифровать) или д (дешифровать): ').lower()
while purpose not in ('ш', 'д'):
    purpose = input('Необходимо ввести в поле - ш (шифровать) или д (дешифровать): ').lower()

language = input('Введите в поле - р (русский) или а (английский): ').lower()
while language not in ('р', 'а'):
    language = input('Необходимо ввести в поле - р (русский) или а (английский): ').lower()

shift = input('Введите шаг сдвига цифрой (сдвиг вправо): ')
while not shift.isdigit():
    shift = input('Ошибка! Введите целое положительное число: ')
shift = int(shift)

question = input('Введите текст для обработки: ')
while not question.strip():
    question = input('Вы не ввели текст! Попробуйте снова: ')

def caesar(question, shift, purpose, language):
    result = ''
    if language == 'р':
        alphabet_lower = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        alphabet_upper = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    else:
        alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
        alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    shift_amount = shift if purpose == 'ш' else -shift

    for char in question:
        if char in alphabet_lower:
            idx = alphabet_lower.index(char)
            new_idx = (idx + shift_amount) % len(alphabet_lower)
            result += alphabet_lower[new_idx]
        elif char in alphabet_upper:
            idx = alphabet_upper.index(char)
            new_idx = (idx + shift_amount) % len(alphabet_upper)
            result += alphabet_upper[new_idx]
        else:
            result += char
    return result

print(caesar(question, shift, purpose, language))