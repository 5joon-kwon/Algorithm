N = int(input())
res = N

for _ in range(N):
    text = input()
    for i in range(len(text) - 1):
        if text[i] == text[i + 1]:
            continue
        else:
            if text[i] in text[i+1:]:
                res -= 1
                break

print(res)