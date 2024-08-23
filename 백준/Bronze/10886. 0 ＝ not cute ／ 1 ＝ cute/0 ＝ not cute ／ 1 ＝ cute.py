N = int(input())

cute = 0
ncute = 0

for _ in range(N):
    opinion = int(input())
    
    if opinion == 0:
        ncute += 1
    else:
        cute += 1
        
if ncute > cute:
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')