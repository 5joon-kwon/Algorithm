import sys

def stack_sequence():
    n = int(sys.stdin.readline())
    stack = []
    answer = []
    cur = 1

    for _ in range(n):
        num = int(sys.stdin.readline().strip())

        while cur <= num:
            stack.append(cur)
            answer.append("+")
            cur += 1

        if stack[-1] == num:
            stack.pop()
            answer.append("-")
        else:
            print("NO")
            return

    print("\n".join(answer))

stack_sequence()
