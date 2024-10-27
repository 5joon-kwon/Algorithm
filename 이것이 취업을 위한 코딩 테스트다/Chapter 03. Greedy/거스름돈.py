# List 활용해 더 유용해진 풀이

N = int(input())

coins = [500, 100, 50, 10]
coin_num = 0

for coin in coins:
    coin_num += N // coin
    N %= coin

print(coin_num)
