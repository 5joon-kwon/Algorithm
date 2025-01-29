li = list(map(int, input().split()))

ascend = sorted(li)
descend = sorted(li, reverse=True)

if li == ascend:
    print('ascending')
elif li == descend:
    print('descending')
else:
    print('mixed')