def solution(numbers, hand):
    
    keypad = {
    1:[0,0], 2:[0,1], 3:[0,2],
    4:[1,0], 5:[1,1], 6:[1,2],
    7:[2,0], 8:[2,1], 9:[2,2],
    '*':[3,0], 0:[3,1], '#':[3,2],
    }
    
    li = keypad['*']
    ri = keypad['#']
    result = ""

    for i in numbers:
        if(i == 1 or i == 4 or i == 7):
            li = keypad[i]
            result += 'L'
        elif(i == 3 or i == 6 or i == 9):
            ri = keypad[i]
            result += 'R'
        else:
            left_distance = abs(li[0] - keypad[i][0]) + abs(li[1] - keypad[i][1])
            right_distance = abs(ri[0] - keypad[i][0]) + abs(ri[1] - keypad[i][1])
            
            if(left_distance > right_distance):
                ri = keypad[i]
                result += 'R'
            elif(left_distance < right_distance):
                li = keypad[i]
                result += 'L'
            else:
                if(hand == "left"):
                    li = keypad[i]
                    result += 'L'
                else:
                    ri = keypad[i]
                    result += 'R'
                    
    return result         