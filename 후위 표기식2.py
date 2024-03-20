n = int(input())
s = list(input())
stack = []
num = []
for i in range(n):
    num.append(int(input()))

for i in s:
    if i.isalpha():
        data = ord(i) - ord('A')
        stack.append(num[data])
    else:
        b = stack.pop()
        a = stack.pop()
        if i == '+':
            stack.append(a+b)
        elif i == '-':
            stack.append(a-b)
        elif i == '*':
            stack.append(a*b)
        elif i =='/':
            stack.append(a/b)

print("%.2f" %stack[0])
