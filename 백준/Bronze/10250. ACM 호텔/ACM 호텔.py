T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    
    floor = N % H
    if floor == 0:
        floor = H
    
    room = N // H
    if floor != H:
        room += 1
    
    if room < 10:
        print(str(floor) + '0' + str(room))
    else:
        print(str(floor) + str(room))