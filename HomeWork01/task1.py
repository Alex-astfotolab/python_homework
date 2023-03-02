x = int(input("Введите 3х значное число: "))
if(x > 99 and x < 999):
    x = str(x)
    print(int(x[0]) + int(x[1]) + int(x[2]))
else:
    print("введено не трехзначное число")