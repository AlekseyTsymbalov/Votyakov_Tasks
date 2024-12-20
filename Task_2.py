def main():
    pass
# Урок два, инструкция if - else
"""Задача 1"""
print("Программа выведет: True")

print("-" * 35)

"""Задача 2"""
USERS_PASSWORD = "8b66bBT67-NVbds8_23dlsa-02EcxjKseQ" # Предположим что пароль уже есть

user_password = input("Enter you password: ")
if user_password == USERS_PASSWORD:
    request = input("Enter you password again: ")
    if request == USERS_PASSWORD:
      print("Welcome!")
else:
    print("Incorrect password!")

print("-" * 65)

"""Задача 3"""
x = int(input("Enter a digit: "))
y = int(input("Enter a digit: "))
c = int(input("Enter a digit: "))
z = int(input("Enter a digit: "))
min_digit = min(x, y, c, z)
print(min_digit)

print("-" * 45)

count = 0
totals = []
while count < 4:
    digits = int(input("Введите число: "))
    totals.append(digits)
    count += 1
print(min(totals))

print("-" * 45)

"""Задача 4"""
x = int(input("Enter a digit: "))
y = int(input("Enter a digit: "))
c = int(input("Enter a digit: "))
z = int(input("Enter a digit: "))
max_digit = max(x, y, c, z)
print(max_digit)

print("-" * 45)

"""Задача 5"""
side_1 = int(input())   #13
side_2 = int(input())   #19
side_3 = int(input())   #15
if side_1 + side_2 > side_3 and side_1 + side_2 > side_3 and side_2 + side_3 > side_1:
    print('True')
else:
    print('False')

print("-" * 45)

"""Задача 6"""
side_1 = int(input())   #10
side_2 = int(input())   #13
side_3 = int(input())   #23
flag = side_1 + side_2 > side_3 and side_1 + side_2 > side_3 and side_2 + side_3 > side_1
if side_1 != side_2 and side_2 != side_3 and side_1 != side_3 and flag:
    print('разносторонний')
if side_1 == side_2 and side_2 == side_3:
    print('равносторонний')
if flag == 0:
    print('вырожденный')

print("-" * 45)

"""Задача 7"""
a = int(input())    # 3
b = int(input())    # 13
c = int(input())    # 7
d = int(input())    # 17

if b < c or d < a:
    print(0)
elif a <= c and d <= b:
    print(d - c + 1)
elif c <= a and b <= d:
    print(b - a + 1)
elif a <= c <= b <= d:
    print(b - c + 1)
elif c <= a <= d and d >= b:
    print(d - a + 1)

if __name__ == "__main__":
    main()
