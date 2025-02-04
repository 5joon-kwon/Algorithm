N = int(input())
have = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

card_dict = {}

for card in have:
    if card in card_dict:
        card_dict[card] += 1
    else:
        card_dict[card] = 1

for m in M_list:
    if m in card_dict:
        print(card_dict[m], end=' ')
    else:
        print(0, end=' ')