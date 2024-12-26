def main():
    pass
# Урок 3 циклы While и for
"""Задача 1"""
x = int(input("Введите число: "))
# while x % 2 != 0 and x % 10 != 0:
while x % 2 == 0 or str(x).endswith("5"):
    x = int(input("Введите число: "))

print("-" * 25)

"""Задача 2"""
for i in range(10):
    print(i, end=" | ")
print()
print("-" * 40)

"""Задача 3"""
numK = int(input("Введите положительное число: "))  # 12345
numN = int(input("Введите положительное число: "))  # 56789
total = 0
while numK <= numN:
    if numK % 2 != 0:
        total += numK
    numK += 1


print(total)

print("-" * 40)

numX = int(input("Введите положительное число: "))  # 12345
numY = int(input("Введите положительное число: "))  # 56789
summa = []
for digit in range(numX, numY + 1):
    if digit % 2 != 0:
        summa.append(digit)


print(sum(summa))

print("-" * 40)

"""Задача 4"""
numberN = int(input("Введите положительное число: ")) # 10
factorial = 1
for n in range(1, numberN + 1):
    factorial = factorial * n

print(factorial)

if __name__ == "__main__":
    main()