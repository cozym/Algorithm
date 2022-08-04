import sys

commend = sys.stdin.readline().rstrip()

stick = []      # 쇠막대기 스택
result = 0

for i in range(len(commend)):
    if commend[i] == '(':
        if commend[i+1] == ')':     # ()가 나온 경우 쇠막대기 스택의 길이만큼 결과에 +
                result += len(stick)
        else:
            stick.append(1)     # ( 가 나온 경우 다음이 )가 아니면 쇠막대기 스택에 push
    elif commend[i] == ')':
        if commend[i-1] != '(':     # )가 쇠막대기의 끝일 경우 pop하여 1만큼 결과에 +
            result += stick.pop()   # ㄴ막대기의 최초값 1을 고려

print(result)