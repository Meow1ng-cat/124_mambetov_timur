Str_Line = input("Введите текст: ")


def dvide_str(str_line):

    formated_string = str()
    word_counter = 0
    word_start = 0
    words_list = []

    for i in range(0, len(str_line) - 2):
        if not(ord(str_line[i]) == 32 and ord(str_line[i+1]) == 32):
            formated_string += str_line[i]

    if len(formated_string) != 0:
        word_counter += 1

    for i in formated_string:
        if ord(i) == 32:
            word_counter += 1

    while len(words_list) != word_counter-1:

        word = str()

        for i in range(word_start, formated_string.find(" ", word_start)):
            if ord(formated_string[i]) != 32:
                word += formated_string[i]

        word_start = (formated_string.find(" ", word_start)+1)
        words_list.append(word)

    word = str()
    for i in range(formated_string.find(" ", formated_string.find(words_list[len(words_list)-1])), len(formated_string)):
        if ord(formated_string[i]) != 32:
            word += formated_string[i]
    words_list.append(word)

    return words_list


def longest_word(word_list):

    word_long_dict = {}

    for i in word_list:
        word_long_dict[len(i)] = i

    return word_long_dict[max(word_long_dict)]


def commonst_word(word_list):

    word_frequency_dict = {}

    for i in word_list:
        equal_word_count = 0
        for j in word_list:
            if i == j:
                equal_word_count += 1
        word_frequency_dict[equal_word_count] = i

    return word_frequency_dict[max(word_frequency_dict)]


print(dvide_str(Str_Line))
print(longest_word(dvide_str(Str_Line)))
print(commonst_word(dvide_str(Str_Line)))
