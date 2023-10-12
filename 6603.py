# 로또
import sys

p = [0 for i in range(6)]

def recursion(S,idx,pointer):
    # arr의 i를 출력 인덱스에 넣을건지 판단
    # 넣었으면 인덱스+1 넘기기 / 안넣었으면 그대로 넘기기
    # 인덱스 수가 6이면 출력하고 리턴
    if idx==6:
        print(*p)
        return
    if pointer >= len(S):
        return
    p[idx] = S[pointer]
    recursion(S,idx+1,pointer+1)
    p[idx] = 0
    recursion(S,idx,pointer+1)

# 0이 나오면 멈춤
while True:
    arr = list(map(int,sys.stdin.readline().split()))
    k = arr[0]
    S = arr[1:]

    if k==0:
        exit(0)

    recursion(S,0,0)
    print()