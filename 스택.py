import sys

N = int(input())

stack = []

def push(X):
    stack.append(X)

def pop():
    if len(stack)==0:
        print(-1)
    else:
        print(stack.pop())

def empty():
    if len(stack)==0:
        print(1)
    else:
        print(0)

def size():
    print(len(stack))

def top():
    if len(stack)==0:
        print(-1)
    else:
        print(stack[len(stack)-1])


for i in range(N):
    commend = sys.stdin.readline().split()

    if commend[0]=="push":
        push(commend[1])
    elif commend[0]=="pop":
        pop()
    elif commend[0]=="size":
        size()
    elif commend[0]=="empty":
        empty()
    elif commend[0]=="top":
        top()
