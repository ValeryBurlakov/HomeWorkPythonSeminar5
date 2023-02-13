a = int(input("Введите число а: "))
b = int(input("Введите число b: "))

operation = 1 # можно и без этой переменной

def sum(a, b):
    if b == 0:
        return a
    return sum(a + operation, b - operation) # арифетические операции "+1" и "-1"
print(f"{a} + {b} равно: {sum(a, b)}")