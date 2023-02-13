# -N...., -4, -3, -2, -1, 0, 1, 2, 3, 4, .......N - целые числа

a = int(input("Введите число, которое хотите возвести в степень: "))
b = int(input("Введите степень с целым показателем: "))


def function(a, b):
    if b == 0:
        return 1
    return a * function(a, b - 1)

if b >=0:
    print(f"{a} в {b} степени равно: {function(a, b)}")
else:
    print(f"{a} в {b} степени равно: 1/{function(a, abs(b))}. То есть: {1/function(a, abs(b))}")




