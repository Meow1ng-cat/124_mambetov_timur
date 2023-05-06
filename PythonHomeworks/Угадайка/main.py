import random

SecretNumber = random.randint(1, 100)
MoveCounter = 0


def game(secretnumber, move_counter):

    while "allegednumber" not in locals():
        try:
            allegednumber = int(input("Угадайте число!\n"))
            if allegednumber < 1 or allegednumber > 100:
                del allegednumber
                print("Ввдеите число от 1 до 100")
        except ValueError:
            print("Введите целое число")

    if secretnumber > allegednumber:
        print("Загаданное число больше")
        move_counter += 1
        game(secretnumber, move_counter)
    elif secretnumber < allegednumber:
        print("Загаданное число меньше")
        move_counter += 1
        game(secretnumber, move_counter)
    else:
        move_counter += 1
        print("Поздравляю вы угадали число! Число было: ", secretnumber, "Ваше кол-во ходов: ", move_counter)


game(SecretNumber, MoveCounter)
