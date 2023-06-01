while "Start" not in globals():
    try:
        Start = int(input("Введите стартовое значение: "))
    except ValueError:
        print("Вы ввели некореткное значение, попробуйте еще раз!")

while "End" not in globals():
    try:
        End = int(input("Введите конечное значение: "))
    except ValueError:
        print("Вы ввели некореткное значение, попробуйте еще раз!")


def sum_range(start, end):

    row_sum = 0

    if start > end:
        start, end = end, start

    for i in range(start, end+1):
        row_sum += i

    return row_sum


print(sum_range(Start, End))
