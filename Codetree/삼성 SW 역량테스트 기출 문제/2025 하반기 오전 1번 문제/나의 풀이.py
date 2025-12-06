# 왼쪽 빼기 가능한 택배 리스트
def left_possible():
    possible_box = set()
    impossible_box = set()
    impossible_i = set()
    for j in range(n):
        for i in range(n):
            # 못나가는 행이면
            if i in impossible_i:
                continue
            
            if grid[i][j] == 0:
                continue
            
            # 택배가 있다면
            if grid[i][j] != 0:
                # 해당 행에 위치한 박스들 이동 불가 처리
                for jj in range(j, n):
                    if grid[i][jj] != 0 and grid[i][jj] != grid[i][j]:
                        impossible_box.add(grid[i][jj])
                        
            # 이동 불가 박스면
            if grid[i][j] in impossible_box:
                continue
            
            # 나갈 수 있는 택배 번호와 행 저장
            possible_box.add(grid[i][j])
            impossible_i.add(i)
            
        # 가능한 행 다 봤으면
        if len(impossible_i) == n:
            break
        
    return possible_box

def right_possible():
    possible_box = set()
    impossible_box = set()
    impossible_i = set()
    # 오른쪽 열부터 보기
    for j in range(n - 1, -1, -1):
        for i in range(n):
            # 못나가는 행이면
            if i in impossible_i:
                continue
            
            if grid[i][j] == 0:
                continue
            
            # 택배가 있다면
            if grid[i][j] != 0:
                # 해당 행에 위치한 박스들 이동 불가 처리
                for jj in range(j, -1, -1):
                    if grid[i][jj] != 0 and grid[i][jj] != grid[i][j]:
                        impossible_box.add(grid[i][jj])
            
            # 이동 불가 박스면
            if grid[i][j] in impossible_box:
                continue
                        
            # 나갈 수 있는 택배 번호와 이동 불가 행 저장
            possible_box.add(grid[i][j])
            impossible_i.add(i)
            
        # 가능한 행 다 봤으면
        if len(impossible_i) == n:
            break
        
    return possible_box
        
# 택배 빼기
def delete(grid, num):
    box = search(num)
    k, ui, di, lj, rj = box
    
    for i in range(ui, di + 1):
        for j in range(lj, rj):
            grid[i][j] = 0
    
    pre_boxes.remove(box)  
    result.append(k)
    
# 택배 채우기
def fill(k, ui, di, lj, rj, grid):
    for i in range(ui, di + 1):
        for j in range(lj, rj):
            grid[i][j] = k

# 특정 택배 위치 정보 찾기
def search(num):
    for box in pre_boxes:
        k, ui, di, lj, rj = box
        if k == num:
            return box
    
# 택배 내리기
def fall():
    # 체크한 상자 담기
    check_li = set()
    
    # 아래부터 보면서
    for i in range(n - 1, -1, -1):
        for j in range(n):
            # 택배 정보 찾아서 내려갈 수 있는지 확인
            if grid[i][j] != 0 and grid[i][j] not in check_li:
                box = search(grid[i][j])
                k, ui, di, lj, rj = box
                check_li.add(k)
                
                # 가장 아래면 다음
                if di + 1 == n:
                    continue
                
                stop_flag = False
                while True:
                    di += 1
                    for wj in range(lj, rj):
                        # 다른 택배 있으면
                        if grid[di][wj] != 0:
                            di -= 1
                            stop_flag = True
                            break
                    
                    # 아래가 비었으면 내리기
                    if not stop_flag:
                        for wj in range(lj, rj):
                            grid[ui][wj] = 0
                        ui += 1
                        
                    # 마지막 줄이면
                    if di + 1 == n:
                        stop_flag = True
                    
                    # 멈춰야하면 격자 채우기
                    if stop_flag:
                        pre_boxes.remove(box)
                        pre_boxes.append([k, ui, di, lj, rj])
                        fill(k, ui, di, lj, rj, grid)
                        break
            

# N x N 격자
n, m = map(int, input().split())
grid = [[0] * n for _ in range(n)]

# 택배 k(번호), h(세로), w(가로), c(상자 왼쪽 열, j - 1)
boxes = [list(map(int, input().split())) for _ in range(m)]
# 낙하 이후 박스 왼쪽 위 좌표 정보 저장
pre_boxes = []
result = []

# 초기 택배 낙하
for k, h, w, j in boxes:
    # 택배 위 행, 아래 행, 왼쪽 열, 오른쪽 열
    ui = 0
    di = ui + (h - 1)
    lj = j - 1
    rj = lj + w
    
    stop_flag = False
    
    # 박스 높이가 격자 높이와 동일할 때
    if h == n:
        pre_boxes.append([k, ui, di, lj, rj])
        fill(k, ui, di, lj, rj, grid)
        continue
    
    while True:
        ui += 1
        di += 1
        for wj in range(lj, rj):
            # 다른 택배 있으면
            if grid[di][wj] != 0:
                ui -= 1
                di -= 1
                stop_flag = True
                break
            
        # 마지막 줄이면
        if di + 1 == n:
            stop_flag = True

        # 멈춰야하면 격자 채우기
        if stop_flag:
            pre_boxes.append([k, ui, di, lj, rj])
            fill(k, ui, di, lj, rj, grid)
            break
                    
# 격자 빌 때까지 반복
while True:
    # 왼쪽으로 택배를 뺄 수 있는 택배 중, k 가 작은 택배 우선 하차
    li = list(left_possible())
    li.sort()

    # 택배 빼기
    delete(grid, li[0])
    
    # 택배 없으면 종료
    if len(pre_boxes) == 0:
        break

    # 택배 낙하 (아래부터 보기)
    fall()

    # 오른쪽으로 택배를 뺄 수 있는 택배 중, k 가 작은 택배 우선 하차
    ri = list(right_possible())
    ri.sort()

    delete(grid, ri[0])
    
    # 택배 없으면 종료
    if len(pre_boxes) == 0:
        break

    # 택배 낙하
    fall()
    

# 하차 택배 번호 순서대로 출력
for r in result:
    print(r)