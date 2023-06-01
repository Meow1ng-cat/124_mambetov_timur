Str_Line = input("Введите текст: ")


def word_counter(str_line):

    formated_string = str()
    counted_words = 0

    for i in range(0, len(str_line) - 2):
        if not (ord(str_line[i]) == 32 and ord(str_line[i + 1]) == 32):
            formated_string += str_line[i]

    if len(formated_string) != 0:
        counted_words += 1

    for i in formated_string:
        if ord(i) == 32:
            counted_words += 1

    return counted_words


print(word_counter(Str_Line))
