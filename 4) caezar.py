while purpose not in ('ш', 'д'):
    purpose = input('Необходимо ввести в поле - ш (шифровать) или д (дешифровать)').lower()

while language not in ('р', 'а'):
    language = input('Необходимо ввести в поле - р (русский) или а (английский)').lower()

shift = input('Введите шаг сдвига цифрой (сдвиг вправо): ')
while not shift.isdigit():
    shift = input('Ошибка! Введите целое положительное число: ')
shift = int(shift)

question = input('Введите текст для обработки: ')
while not question.strip():  
    question = input('Вы не ввели текст! Попробуйте снова: ')


