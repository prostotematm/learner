First = input('Введите первое число: ')
Second = input('Введите первое число: ')
Third = input('Введите первое число: ')


if First == Second and First == Third and Second == Third:
    print("3")
elif First == Second or First == Third or Second == Third:
    print("2")
else:
    print("0")