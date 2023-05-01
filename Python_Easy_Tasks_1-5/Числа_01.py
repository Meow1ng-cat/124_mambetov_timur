import random

while "X" not in globals():
    try:
        X = int(input("Введите число Х: "))
        if X < 0:
            del X
            print("Вы должны ввести число больше нуля")
    except ValueError:
        print("Вы должны ввести целочисленное число")

List_1 = []
for i in range(random.randint(5, 100)):
    List_1.append(random.randint(0, 9999))


def magic(x, list_1):
    list_sum = sum(list_1)
    if list_sum % x == 0:
        return True
    else:
        return False


print(len(List_1))
print(List_1)
print(magic(X, List_1))
