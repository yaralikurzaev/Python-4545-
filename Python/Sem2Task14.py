def powers_of_two(n):
    k = 0
    while 2**k <= n:
        print(2**k)
        k += 1

# пример использования
powers_of_two(50)
