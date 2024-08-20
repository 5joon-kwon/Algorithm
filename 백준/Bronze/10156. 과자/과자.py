price, num, money = map(int, input().split())

tot = price * num

if tot > money:
    print(tot - money)
else:
    print(0)