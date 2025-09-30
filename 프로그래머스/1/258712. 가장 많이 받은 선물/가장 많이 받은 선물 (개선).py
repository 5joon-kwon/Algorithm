def solution(friends, gifts):
    n = len(friends)
    idx = {name: i for i, name in enumerate(friends)}  # name -> 0..n-1

    # 주고받은 횟수 행렬
    sent = [[0]*n for _ in range(n)]

    # 개인별 준/받은 개수
    give_cnt = [0]*n
    get_cnt  = [0]*n

    # 기록 파싱
    for g in gifts:
        a, b = g.split()
        i, j = idx[a], idx[b]
        sent[i][j] += 1
        give_cnt[i] += 1
        get_cnt[j]  += 1

    # 선물 지수
    score = [give_cnt[i] - get_cnt[i] for i in range(n)]

    # 다음 달 받는 선물 개수
    next_month = [0]*n

    # 각 쌍(i, j)은 i < j만 비교 ⇒ 중복 방지
    for i in range(n):
        for j in range(i+1, n):
            if sent[i][j] > sent[j][i]:
                next_month[i] += 1
            elif sent[i][j] < sent[j][i]:
                next_month[j] += 1
            else:
                if score[i] > score[j]:
                    next_month[i] += 1
                elif score[i] < score[j]:
                    next_month[j] += 1
                # 같으면 아무도 못 받음

    return max(next_month) if n > 0 else 0
