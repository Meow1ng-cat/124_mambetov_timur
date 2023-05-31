Sentence = input("Введите предложения которе надо сделать крутым: ")


def fency_style(sentence):

    cooler_sentence = str()
    pre_is_low = False

    for i in sentence:
        if ord(i) > 64:
            if pre_is_low:
                cooler_sentence += i.upper()
                pre_is_low = False
            else:
                cooler_sentence += i.lower()
                pre_is_low = True
        else:
            cooler_sentence += i

    return cooler_sentence


print(fency_style(Sentence))
