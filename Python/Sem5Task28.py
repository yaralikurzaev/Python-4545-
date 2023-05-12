def sum_recursive(a, b):
    if b == 0:
        return a
    elif a == 0:
        return b
    else:
        return sum_recursive(a + 1, b - 1)

# Пример использования:
number_a = int(input("Введите число A: "))
number_b = int(input("Введите число B: "))

result = sum_recursive(number_a, number_b)
print(f"Сумма: {result}")