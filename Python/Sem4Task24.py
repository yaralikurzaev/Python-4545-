def max_berry_harvest(N, ai):
    dp = [[0] * N for _ in range(N)]

    # Заполняем первую строку массива dp
    for j in range(N):
        dp[0][j] = ai[j]

    # Заполняем остальные строки массива dp
    for i in range(1, N):
        for j in range(N):
            dp[i][j] = max(dp[i-1][(j-1) % N], dp[i-1][j], dp[i-1][(j+1) % N]) + ai[j]

    # Находим максимальное значение в последней строке массива dp
    max_harvest = max(dp[N-1])

    return max_harvest


# Ввод данных от пользователя
N = int(input("Введите количество кустов: "))
ai = list(map(int, input("Введите количество ягод на каждом кусте через пробел: ").split()))

# Вызов функции и вывод результата
result = max_berry_harvest(N, ai)
print("Максимальное количество собранных ягод:", result)


