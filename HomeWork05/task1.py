def deg(a, b):
    res = 1
    i = 0
    while i < b:
        res = res * a
        i = i + 1
        
        if(i == b):
            return res
        


x = int(input("введите число: "))
y = int(input("введите желаемую степень числа: "))

print(deg(x, y))