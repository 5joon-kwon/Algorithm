li = input()
bomb = input()

# 전체 문자열을 while 문으로 반복해서 검사하면 시간초과 !
# stack에 문자열을 하나씩 집어넣으면서 폭발 문자열을 검사하면 된다 !
stack = []

for i in li:
    stack.append(i)
    # list의 맨뒤 요소부터 폭발 문자열의 길이만큼을 문자열로 바꿨을 때, 폭발 문자열과 같다면 ?
    if ''.join(stack[-len(bomb):]) == bomb:
        del stack[-len(bomb):] # list에서 폭발 문자열 요소를 삭제

res = ''.join(stack)

if res == '':
    print('FRULA')
else:
    print(res)
