#알파벳 개수 (10808)
stack = [0 for i in range(26)]
str = input()

for i in str:
    stack[ord(i)-97] += 1

print(*stack)