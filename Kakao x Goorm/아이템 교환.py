N, M = map(int, input().split())
goorm = input().split()
friend = input().split()

print(goorm, friend)
for _ in range(M):
	a, b = input().split()
	if a in goorm and b in friend:
		goorm.remove(a)
		goorm.append(b)
		friend.remove(b)
		friend.append(a)
	
	goorm.sort()

print(goorm)