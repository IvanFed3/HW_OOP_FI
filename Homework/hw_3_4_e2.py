n = int(input('Введіть розмір квадрату цілим числом:'))
if n == 1:
    print('#', end='')
elif n > 1:
    for i in range(n):
        if i == n-1 or i == 0:
            for j in range(n):
                print('#', end='')
            print('')
        else:
            print("#", end="")
            for j in range(n-2):
                print(" ", end="")
            print("#", end="")
            print('')
