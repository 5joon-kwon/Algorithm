import sys

while True:
    name, age, weight = sys.stdin.readline().split()
    if name == '#':
        break
    if int(age) > 17 or int(weight) >= 80:
        print(f'{name} Senior')
    else:
        print(f'{name} Junior')
