while "JerrySpeed" not in globals():
    try:
        JerrySpeed = int(input("Введите скорость Джерри: "))
        if JerrySpeed < 0:
            del JerrySpeed
            print("Вы должны ввести число больше нуля")
    except ValueError:
        print("Вы должны ввести целочисленное число")

while "TomSpeed" not in globals():
    try:
        TomSpeed = int(input("Введите скорость Тома: "))
        if TomSpeed < 0:
            del TomSpeed
            print("Вы должны ввести число больше нуля")
    except ValueError:
        print("Вы должны ввести целочисленное число")

while "Distance" not in globals():
    try:
        Distance = int(input("Введите расстояние между Томом и Джерри: "))
        if Distance < 0:
            del Distance
            print("Вы должны ввести число больше нуля")
    except ValueError:
        print("Вы должны ввести целочисленное число")


def race(jerry_speed, tom_speed, distance):
    if (tom_speed > jerry_speed) and (distance > 0):
        time_to_cache = distance / (tom_speed - jerry_speed)
        return time_to_cache
    elif (tom_speed <= jerry_speed) and (distance > 0):
        return "Том не поймает Джерри"
    else:
        return "Том уже поймал Джерри"


print(race(JerrySpeed, TomSpeed, Distance))
