num = int(input())

stack = []

for i in range(num):
    stack.append([])
    stack[i] = input().split(" ")
    
for j in range(num):
    for x in range(len(stack[j])):
        print(stack[j][x][::-1],end=' ')
    if j != num-1:
        print("")