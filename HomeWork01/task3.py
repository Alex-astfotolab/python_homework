x = int(input("Введите номер билетика, 6 цифр: "))

if(x < 999999 and x > 99999):
    x = str(x)
    a = int(x[0]) + int(x[1]) + int(x[2])
    b = int(x[3]) + int(x[4]) + int(x[5])
    if(a == b):
        print(f'Билет № {x} счастливый')
    if(a != b):
        print(f'Билет № {x} не счастливый')
else:
    print(f'Билет № {x} не из 6 цифр')