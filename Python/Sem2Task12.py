import math

def solve_equation(s, p):
    D = s ** 2 - 4 * p
    if D < 0:
        return None
    x = (s + math.sqrt(D)) / 2
    y = (s - math.sqrt(D)) / 2
    return (x, y)

# пример использования
s = 10
p = 24
result = solve_equation(s, p)
if result is None:
    print("Решений нет")
else:
    print("Результат:", result) # Выведет (6.0, 4.0), т.к. 6+4=10 и 6*4=24