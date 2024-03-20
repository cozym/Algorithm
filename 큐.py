import sys

queue = []

for i in range(int(sys.stdin.readline())):
    commend = sys.stdin.readline().split()

    if commend[0] == "push":
        queue.append(commend[1])
    elif commend[0] == "pop":
        if queue:
            print(queue.pop(0))
        else:
            print(-1)
    elif commend[0] == "size":
        print(len(queue))
    elif commend[0] == "empty":
        if queue:
            print(0)
        else:
            print(1)
    elif commend[0] == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif commend[0] == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)