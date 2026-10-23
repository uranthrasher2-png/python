number = int(input('Введите число в десятичной системе счисления'))
osn = int(input('Введите в какую систему счисления перевести число'))

ost=''
cel = number // osn
while cel>0:
    ost+= str(number % osn)
    number=cel
    cel//= osn
ost=ost+(str(number % osn))
ost=ost[::-1]
print(ost)

