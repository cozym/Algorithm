# 알파벳 찾기 (10809)
str = input()
stack = [-1 for i in range(26)]

for j in range(len(str)):
    if(stack[ord(str[j])-97])==-1:
        stack[ord(str[j])-97] = j

print(*stack)