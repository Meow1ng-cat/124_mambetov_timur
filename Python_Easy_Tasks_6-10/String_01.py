Substr = input("Введите строку в которой будет поиск: ")
St = input("Ввдеите искомую строку: ")


def search_substr(subst, st):
    if (subst.lower()).find(st.lower()) >= 0:
        print("Есть контакт!")
    else:
        print("Мимо!")


search_substr(Substr, St)