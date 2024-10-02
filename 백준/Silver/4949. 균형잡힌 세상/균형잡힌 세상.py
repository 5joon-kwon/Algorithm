while True:
    left = []
    flag = 0
    
    s = input()
    if s == '.':
        break
    else:
        sentence = s.replace(" ", "")
        for i in sentence:
            if i == '(' or i == '[':
                left.append(i)
            elif i == ')' or i == ']':
                if len(left) == 0:
                    print('no')
                    flag = 1
                    break
                l = left.pop()
                if i == ')' and l != '(':
                    print('no')
                    flag = 1
                    break
                elif i == ']' and l != '[':
                    flag = 1
                    print('no')
                    break
    if flag == 1:
        continue
    elif len(left) != 0:
        print('no')
    elif len(left) == 0:
        print('yes')            