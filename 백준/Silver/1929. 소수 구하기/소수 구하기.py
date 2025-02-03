M, N = map(int, input().split())

def is_prime(N):
    # 1 ~ N 까지 모두 판별하기 위해 N + 1개 index 설정정
    prime = [True] * (N + 1)
    # index 0, 1은 소수가 아니므로 False 처리
    prime[0] = prime[1] = False
    
    # 2부터 N의 제곱근까지 소수 판별별
    for i in range(2, int(N ** 0.5) + 1):
        # i 번째 숫자가 True (소수) 이면
        if prime[i]:
            # i * i 시작 : 이전 소수의 배수로 지운 값들을 중복해서 검사하지 않기 위해
            # step = i : 마찬가지로 중복하여 검사하지 않기 위해 소수 i 의 배수만 검사
            for j in range(i * i, N + 1, i):
                prime[j] = False
    
    return prime

prime_list = is_prime(N)

for i in range(M, N + 1):
    # True(소수)이면 출력력
    if prime_list[i]:
        print(i)