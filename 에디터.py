import sys

stack_1 = list(sys.stdin.readline().rstrip())
stack_2 = []

for i in range(int(sys.stdin.readline())):
    commend = sys.stdin.readline().split()

    if commend[0] == "P":
        stack_1.append(commend[1])
    elif commend[0] == "L":
        if stack_1:
            stack_2.append(stack_1.pop())
    elif commend[0] == "D" :
        if stack_2:
            stack_1.append(stack_2.pop())
    elif commend[0] == "B":
        if stack_1:
            stack_1.pop()

stack_1.extend(reversed(stack_2))
print("".join(stack_1))