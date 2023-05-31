Supply = []
Demand = []

while "Number_of_objects" not in locals():
    try:
        Number_of_objects = int(input("Ввдедите кол-во объектов: "))
        if Number_of_objects < 0:
            print("Введите значение больше нуля!")
            del Number_of_objects
    except ValueError:
        print("Вы ввели некоретктное значение, попробуйте еще раз!")


def input_func(list_for_fill):

    for i in range(0, Number_of_objects):
        input_value = input()
        list_for_fill.append(input_value)

    return list_for_fill


print("Введите значение предложения")
Supply = input_func(Supply)
print("Введите значение спроса")
Demand = input_func(Demand)


def when_equal(supply, demand):

    equal_counter = 0

    for i in range(0, Number_of_objects):
        if supply[i] == demand[i]:
            equal_counter += 1

    return equal_counter


print(when_equal(Supply, Demand))
