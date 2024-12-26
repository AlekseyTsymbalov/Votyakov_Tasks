def main():
    pass
"""Задача 1"""
n = int(input("Enter digit: "))
a = [0]
for i in range(n):
    x = int(input())
    a = [i] * x
print(f"Вывод будет 2 2 2 == {a}")

print("-" * 45)

"""Задача 2"""
n1 = int(input("Enter digit: "))
a = []
for j in range(n1):
    a = a + [j] * j
print(f"Вывод будет 1 2 2 == {a}")

print("-" * 45)

"""Задача 3"""
n2 = int(input("Enter digit 5: ")) # 5
array_num = []
for x in range(n2):
    num = int(input(f"Input: {x + 1} ")) # 2, 3, 1, 5, 10
    array_num.append(num)

print(sum(array_num) / len(array_num))

print("-" * 45)

"""Конечно можно через библиотеку statistics вс сделать, тоже рабочий вариант"""
from statistics import mean

n3 = int(input("Enter digit 5: ")) # 5
array_num = []
for z in range(n3):
    num = int(input(f"Input: {z + 1} ")) # 2, 3, 1, 5, 10
    array_num.append(num)

average = mean(array_num)
print(average)

print("-" * 45)

"""Задача 4"""
n4 = int(input("Введите число: "))
m = int(input("Введите число для индекса: "))
# for k in range(n4): # Заморочка! Лучше так...
index_element = list(map(int, input(f"Введите {n4} чисел, разделённых пробелом: ").split()))
if 0 <= m < n4:
    print(f"Элемент с индексом m: {index_element[m]}")
else:
    print("Индекс m выходит за пределы массива.")

print("-" * 45)

"""Задача 5"""
n5 = int(input("Введите число: "))
sum_array = list(map(int, input(f"Введите {n5} чисел, разделённых пробелом: ").split()))
totals = sum(sum_array[::2])
print(totals)

print("-" * 45)

num = int(input("Enter digit: "))
digit = []
for i in range(num):
    elem = int(input("Input digit: "))
    digit.append(elem)

print(digit)
print(sum(digit[::2]))


if __name__ == "__main__":
    main()
