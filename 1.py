def reverse(s):
    if len(s) != 0:
        print(s[-1], end="")
        reverse(s[:-1])
    else:
        return

string = input("Введіть слово: ")
reverse(string)
