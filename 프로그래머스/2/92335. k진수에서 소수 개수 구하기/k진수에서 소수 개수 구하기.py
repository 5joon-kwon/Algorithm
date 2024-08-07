def solution(n, k):
    kdigit = ''
    count = 0
    
    while n > 0:                    # 몫 > 0 까지
        n, mod = divmod(n, k)       # n을 k로 나눠서 몫 = n, 나머지 = k
        kdigit = str(mod) + kdigit  # '1' + '1110' 처럼 left에 붙여주기
        
    digit_list = kdigit.split('0')  # '0'으로 split
    for i in digit_list:
        if i and is_prime(int(i)):  # 소수판별
            count += 1
            
    return count

def is_prime(num):
    if num < 2:                     # 1은 소수 아님
        return False

    for i in range(2,int(num ** 0.5) + 1): # 2부터 어떤 수의 제곱근까지 약수가 있으면 소수 x
        if num % i == 0:
            return False
        
    return True
            