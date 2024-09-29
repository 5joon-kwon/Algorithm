N = list(input())

N.sort()
N.reverse()
res = ('').join(N)

print(int(res))

# 효율적인 코드

# print(int(''.join(sorted(list(input()), reverse = True))))