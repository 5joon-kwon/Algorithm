# 내가 생각한 풀이
hour, min, sec = map(int, input().split())
cook = int(input())

s = cook % 60
m = cook // 60
h = cook // 60 // 60
m -= h * 60

hour += h
min += m
sec += s

while True:
    if sec >= 60:
        min += 1
        sec -= 60

    if min >= 60:
        hour += 1
        min -= 60
        
    if hour >= 24:
        hour -= 24

    if sec < 60 and min < 60 and hour < 24:
        break

print(hour, min ,sec)

# 쉬운 풀이
hour, min, sec = map(int, input().split())
cook = int(input())

sec += cook
min = sec // 60
sec %= 60        # 60초 다음은 0초

hour = min // 60
min %= 60        # 60분 다음은 0분

hour %= 24       # 24시 다음은 0시

print(hour, min, sec)

