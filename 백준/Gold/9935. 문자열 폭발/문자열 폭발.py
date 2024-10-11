li = input()
bomb = input()

stack = []

for i in li:
    stack.append(i)
    if ''.join(stack[-len(bomb):]) == bomb:
        del stack[-len(bomb):]

res = ''.join(stack)
if res == '':
    print('FRULA')
else:
    print(res)