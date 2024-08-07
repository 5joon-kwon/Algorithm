def solution(board, moves):
    li = []
    count = 0
    idx = -1
        
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                li.append(board[j][i-1])
                board[j][i-1] = 0
                idx += 1
                break
                
        if (idx > 0) and (li[idx] == li[idx-1]):
            li.pop()
            li.pop()
            idx -= 2
            count += 2  
            
    answer = count
    return answer