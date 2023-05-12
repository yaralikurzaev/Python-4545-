def power_recursive(a, b):
    if b == 0:
        return 1
    elif b < 0:
        return 1 / power_recursive(a, -b)
    elif b % 2 == 0:
        temp = power_recursive(a, b // 2)
        return temp * temp
    else:
        return a * power_recursive(a, b - 1)

# Пример использования:
number_a = int(input("Введите число A: "))
number_b = int(input("Введите степень B: "))

result = power_recursive(number_a, number_b)
print(f"Результат: {result}")