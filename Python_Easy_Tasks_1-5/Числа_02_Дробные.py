while "A" not in globals():
    try:
        A = float(input("Введите A: "))
        if A <= 1000 or A >= 99999 or A % 1 == 0:
            del A
            print("Введите дробное число меньше 99999 и больше 1000")
    except ValueError:
        print("Ввдеите дробное число")

while "B" not in globals():
    try:
        B = float(input("Введите B: "))
        if B <= 1000 or B >= 99999 or B % 1 == 0:
            del B
            print("Введите дробное число меньше 99999 и больше 1000")
    except ValueError:
        print("Ввдеите дробное число")

while "C_check" not in globals():
    try:
        C_check = float(input("Введите сумму А и B: "))
        if C_check <= 2000 or C_check >= 199998:
            del C_check
            print("Введите дробное число меньше 199998 и больше 2000")
    except ValueError:
        print("Ввдеите дробное число")


def eqv(a, b, c_check):
    c = a + b
    if a > b:
        if (c-(a*0.0001) < c_check) and (c_check < c+(a*0.0001)):
            return True
        else:
            return False
    else:
        if (c-(b*0.0001) < c_check) and (c_check < c+(b*0.0001)):
            return True
        else:
            return False


print(eqv(A, B, C_check))


