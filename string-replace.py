GLOBAL_VAR = ""


def replace_word():
    str = "Hi! My name is John!"
    old_word = input("Enter the word you want to replace: ")
    new_word = input("Enter the word you want to insert intead: ")
    print(str.replace(old_word, new_word))  # Case Sensitive


def main():
    replace_word()


if __name__ == "__main__":
    main()
