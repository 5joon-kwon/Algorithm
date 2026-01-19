N = int(input())
price = list(map(int, input().split()))

mini = price[0]
maxi = 0

for p in price[1:]:
    maxi = max(maxi, p - mini)

    if p < mini:
        mini = p

print(maxi)