import os

Directory = input("Введите вашу диреторию: ")


def print_docs(directory):
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path):
            print(item_path)
        else:
            print_docs(item_path)


print(print_docs(Directory))