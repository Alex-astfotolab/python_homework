def sum(a, b):
    a+= 1
    b-= 1

    if b > 0:
        return sum(a, b)
    else:
        return a
    
x = int(input("введите первое число: "))
y = int(input("введите второе число: "))

print(f'сумма чисел', sum(x, y))