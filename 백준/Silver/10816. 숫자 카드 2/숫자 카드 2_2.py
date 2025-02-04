N = int(input())
# 이분 탐색을 위해 list 정렬
have = sorted(list(map(int, input().split())))
M = int(input())
M_list = list(map(int, input().split()))

card_dict = {}

for card in have:
    if card in card_dict:
        card_dict[card] += 1
    else:
        card_dict[card] = 1

# 이분 탐색
def Binary_Search(card):
    start, end = 0, N - 1
    while start <= end:
        mid = (start + end) // 2
        if card == have[mid]:
            return card_dict[card]
        elif card > have[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return 0

for card in M_list:
    print(Binary_Search(card), end=' ')