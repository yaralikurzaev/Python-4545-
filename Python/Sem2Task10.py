def min_coin_flips(coins):
    heads = coins.count('H')
    tails = coins.count('T')
    return min(heads, tails)

coins = ['H', 'T', 'T', 'H', 'H']
print(min_coin_flips(coins)) # Выведет 2, так как нужно перевернуть две монеты T, чтобы получить все монеты в одном положении
