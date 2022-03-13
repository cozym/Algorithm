import sys

commend = sys.stdin.readline().rstrip()

stick = []      # 쇠막대기 스택
result = 0

def addone(n):
    return n+1

for i in range(len(commend)):
    if commend[i] == '(':
        if commend[i+1] == ')':     # ()가 나온 경우 쇠막대기 스택의 각 요소에 +1
            for j in range(len(stick)):
                stick[j] += 1
        else:
            stick.append(1)     # ( 가 나온 경우 다음이 )가 아니면 쇠막대기 push
    elif commend[i] == ')':
        if commend[i-1] != '(':     # )가 레이저가 아닌 경우 쇠막대기 pop하여 결과에 합연산
            result += stick.pop()

print(result)