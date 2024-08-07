hour, min = map(int, input().split())
time = int(input())

min += (time % 60)
hour += (time // 60)

while min >= 60:
    hour += 1
    min -= 60
    
if hour >= 24:
    hour -= 24
    
print(hour, min)