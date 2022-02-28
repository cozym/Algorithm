import sys

f_deque = []
b_deque = []

for i in range(int(sys.stdin.readline())):
    commend = sys.stdin.readline().split()

    if commend[0] == "push_front":
        f_deque.append(commend[1])
    elif commend[0] == "push_back":
        b_deque.append(commend[1])
    elif commend[0] == "pop_front":
        if f_deque:
            print(f_deque.pop())
        elif b_deque:
            print(b_deque.pop(0))
        else:
            print(-1)
    elif commend[0] == "pop_back":
        if b_deque:
            print(b_deque.pop())
        elif f_deque:
            print(f_deque.pop(0))
        else:
            print(-1)
    elif commend[0] == "size":
        print(len(f_deque)+len(b_deque))
    elif commend[0] == "empty":
        if f_deque or b_deque:
            print(0)
        else:
            print(1)
    elif commend[0] == "front":
        if f_deque:
            print(f_deque[-1])
        elif b_deque:
            print(b_deque[0])
        else:
            print(-1)
    elif commend[0] == "back":
        if b_deque:
            print(b_deque[-1])
        elif f_deque:
            print(f_deque[0])
        else:
            print(-1)