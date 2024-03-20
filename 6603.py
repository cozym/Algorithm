# 로또
import sys

p = [0 for i in range(6)]

def recursion(S,idx,pointer):
    if idx==6:  # 출력조건
        print(*p)
        return
    if pointer >= len(S):   # 인덱스를 계속 채택하지 않을 경우 예외처리
        return
    p[idx] = S[pointer]
    recursion(S,idx+1,pointer+1)    # 인덱스를 채택한 경우
    p[idx] = 0
    recursion(S,idx,pointer+1)  # 채택하지 않은 경우

# 0이 나오면 멈춤
while True:
    arr = list(map(int,sys.stdin.readline().split()))
    k = arr[0]
    S = arr[1:]

    if k==0:
        exit(0)

    recursion(S,0,0)
    print()