N = int(input())

p_stack = []
p_str = []

def push():
    p_stack.append(1)

def pop():
    if len(p_stack) == 0:
        p_stack.append(-1)
        return -1
    else:
        p_stack.pop()

for i in range(N):
    p_str.append([])
    p_str[i] = input()

for x in range(N):
    for y in range(len(p_str[x])):
        if p_str[x][y] == '(':
            push()
        else:
            if pop() == -1:
                break
    if len(p_stack) == 0:
        print("YES")
    else:
        print("NO")
    p_stack = []