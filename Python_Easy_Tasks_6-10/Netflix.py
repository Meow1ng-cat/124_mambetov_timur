while "Alice_Money" not in globals():
    try:
        Alice_Money = int(input("Ввдеите количесво денег Алисы: "))
    except ValueError:
        print("Вы ввели некоректное значение")

while "Bob_Money" not in globals():
    try:
        Bob_Money = int(input("Ввдеите количесво денег Боба: "))
    except ValueError:
        print("Вы ввели некоректное значение")

while "Charlie_Money" not in globals():
    try:
        Charlie_Money = int(input("Ввдеите количесво денег Чарли: "))
    except ValueError:
        print("Вы ввели некоректное значение")

while "Cost" not in globals():
    try:
        Cost = int(input("Ввдеите Цену подписки: "))
    except ValueError:
        print("Вы ввели некоректное значение")


def who_can_buy(alice_money, bob_money, charlie_money, cost):

    alice_and_bob = cost - (alice_money + bob_money)
    alice_and_charlie = cost - (alice_money + charlie_money)
    bob_and_charlie = cost - (bob_money + charlie_money)
    combination_list = [alice_and_bob, alice_and_charlie, bob_and_charlie]

    for i in combination_list:
        if i < 0:
            combination_list.remove(i)

    if min(combination_list) == alice_and_bob:
        print("Алиса и Боб могут купить подписку")
    elif min(combination_list) == alice_and_charlie:
        print("Алиса и Чарли могут купить подписку")
    elif min(combination_list) == bob_and_charlie:
        print("Боб и Чарли могут купить подписку")
    elif alice_and_bob+charlie_money > 0:
        print("Подписку можно купить только если скинутся все!")
    else:
        print("На подписку не хватает денег")


who_can_buy(Alice_Money, Bob_Money, Charlie_Money, Cost)
