print('Перевод из 2-й системы счисления в 10-ю')
value = input('Введите число системе счисления ')
osn = int(input('Введите основание системы счисления '))


alpha = {
    'A': 10, 'B': 11, 'C': 12,
    'D': 13, 'E': 14, 'F': 15
}

numbers = []

for char in value:
    if char.isdigit():
        numbers.append(int(char))
    elif char in alpha:
        numbers.append(alpha[char])

numbers = numbers[::-1]
itog = 0
for i in range(len(numbers)):
    itog += int(numbers[i]) * (osn ** i)
print(itog)
