def collatz(number):
    if number % 2 == 0:
        result = number//2
        print(result)
        return result
    elif number % 2 == 1:
        result = 3*number+1
        print(result)
        return result


try:
    print('Введите целое число')
    digit = int(input())
    if  digit  <= 0:
        print("Ошибка: число должно быть больше нуля!")
    else:    
        while digit != 1:
            digit = collatz(digit)
except ValueError:
    print('Необходимо ввести целое число, а не буквы')
