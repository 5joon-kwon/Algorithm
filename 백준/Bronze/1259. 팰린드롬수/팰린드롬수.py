while True:
    num = input()
    
    if num == '0':
        break
    
    num_reverse = num[::-1]
    
    if num == num_reverse:
        print('yes')
    else:
        print('no')