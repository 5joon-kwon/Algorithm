def solution(m, n, board):
    board2 = []
    location = set()
    block = 0
    for i in board:
        board2.append(list(i))   
    
    while True:
        for i in range(m - 1): # 끝열 전까지
            for j in range(n - 1):  # 끝행 전까지
                if board2[i][j] == '':
                    continue
                elif board2[i][j] == board2[i][j+1] == board2[i+1][j] == board2[i+1][j+1]:
                    location.update([(i,j),(i,j+1),(i+1,j),(i+1,j+1)]) # 4개 같으면 좌표 추가
                    # set(집합)은 중복이 안되므로 유용함
        if location:                # 4개 이상 같은 블록이 한번도 없으면 실행 x
            block += len(location)  # 있다면 좌표의 길이가 곧 같은 블록의 수
            for i, j in location:
                board2[i][j] = ''   # 좌표의 값을 빈 문자열로 두기
            location = set()        # 위의 과정 다시 진행하기 위해 집합 초기화
        else:
            break
        
        while True:                 # 빈 곳에 블록 내리기
            move = 0                # 블록이 움직였는지 확인하기 위한 flag
            for i in range(m - 1):  # 끝열 전까지만 확인
                for j in range(n):  # 모든 행 다 봐야함
                    if board2[i][j] != '' and board2[i+1][j] == '':
                        # 현재 위치가 문자고, 다음 열이 비어있다면
                        board2[i][j], board2[i+1][j] = board2[i+1][j], board2[i][j]
                        # 둘의 위치 바꾸기
                        move = 1    # 변경 사항 있다고 flag 바꾸기
            if move == 0:   # 변동이 없다면 종료
                break
    
    return block