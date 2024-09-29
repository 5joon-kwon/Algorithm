import sys

N = int(input())
num = []

for _ in range(N):
    # 반복문을 통해서 입력 받을 때 : sys.stdin.readline()으로 '\n'까지 한번에 받아 처리해 시간 줄이자.
    num.append(int(sys.stdin.readline()))

num.sort()

for i in num:
    print(i)
