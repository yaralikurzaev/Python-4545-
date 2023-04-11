# вводим номер билета
number = input("Введите номер билета (6 цифр): ")

# проверяем, что номер состоит из 6 цифр
if len(number) != 6 or not number.isdigit():
    print("Некорректный номер билета")
else:
    # разбиваем номер на три числа по две цифры
    n1 = int(number[0])
    n2 = int(number[1])
    n3 = int(number[2])
    n4 = int(number[3])
    n5 = int(number[4])
    n6 = int(number[5])

    # проверяем условие счастливого билета
    if n1 + n2 + n3 == n4 + n5 + n6:
        print("Счастливый билет")
    else:
        print("Обычный билет")
