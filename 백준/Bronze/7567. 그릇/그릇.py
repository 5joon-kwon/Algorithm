plate = input()
height = 10

for i in range(len(plate) - 1):
    if plate[i+1] == plate[i]:
        height += 5
    else:
        height += 10

print(height)