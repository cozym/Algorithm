list = []
stack = []
result = []
next = 0

N = int(input(""))

for i in range(N):
    list.append(int(input("")))
    if next < list[i]:
        for j in range(list[i]-next):
            result.append("+")
            next += 1
            stack.append(next)
        result.append("-")
        stack.pop()
    elif len(stack) == 0 or (stack[-1] < list[i] and list[i] < next):
        print("NO")
        break
    elif list[i] <= stack[-1]:
        while(True):
            result.append("-")
            if stack.pop() == list[i]:
                break
    if i == N-1:
        for j in result:
            print(j)