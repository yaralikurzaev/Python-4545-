def find_common_elements(n, m):
    set1 = set()
    set2 = set()

    # Ввод элементов первого множества
    print("Введите элементы первого множества:")
    for i in range(n):
        num = int(input())
        set1.add(num)

    # Ввод элементов второго множества
    print("Введите элементы второго множества:")
    for i in range(m):
        num = int(input())
        set2.add(num)

    # Находим пересечение множеств
    common_elements = set1.intersection(set2)

    # Выводим результаты
    print("Общие элементы в порядке возрастания:")
    for num in sorted(common_elements):
        print(num)


# Получаем входные данные от пользователя
n = int(input("Введите количество элементов первого множества: "))
m = int(input("Введите количество элементов второго множества: "))

# Вызываем функцию для поиска общих элементов и их вывода
find_common_elements(n, m)
