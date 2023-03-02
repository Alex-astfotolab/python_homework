n = int(input("введите n: "))
m = int(input("введите m: "))
k = int(input("введите k: "))
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('да')
else:
    print('нет')