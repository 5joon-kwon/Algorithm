def cal(n, count):
    count = 0
    while n != 1:
        if n % 2 == 0:
            n//=2
        else:
            n = (n-1)//2
        count += 1
    return count
def solution(num_list):
    count = 0
    for i in num_list:
        count += cal(i, count)
    return count