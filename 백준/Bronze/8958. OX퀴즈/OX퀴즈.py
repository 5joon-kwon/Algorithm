case = int(input())

for _ in range(case):
    ox = input()
    score = 0
    tot = 0
    for i in range(len(ox)):
        if ox[i] == 'O':
            score += 1
        else:
            score = 0
        tot += score
    print(tot)