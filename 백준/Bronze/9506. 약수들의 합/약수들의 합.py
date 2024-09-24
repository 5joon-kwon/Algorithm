def find_divisors(number):
	divisors = []
	for i in range(1, int(number ** 0.5) + 1): # 1 ~ number의 제곱근까지만 탐색
		if number % i == 0: # 나머지가 0이면 약수이다.
			divisors.append(i)
			if i != (number // i): # 나누는 값과 몫이 다르면 (4 x 4 가 아니면)
				divisors.append(number // i) # number // i 는 i에 대응하는 약수
	
	divisors.sort()
	
	return divisors

while True:
    n = int(input())
    
    if n == -1:
        break
    else:
        res = find_divisors(n)
        res = res[:-1]  # 자기 자신은 제외
        
        if sum(res) == n:
            res_string = (' + ').join(map(str, res)) # int 리스트를 문자열로 변환
            print(f'{n} = {res_string}')
            
        else:
            print(f'{n} is NOT perfect.')
