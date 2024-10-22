# 팰린드롬?
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
dp = [([0]*N) for _ in range(N)]

for l in range(N):  # 0~N 의 길이 체크
    for s in range(N-l):    # 시작 idx
        e = s + l   # 끝 idx
        if s == e:  # 한개인 문자열 펠린드롬
            dp[s][e] = 1
        elif arr[s] == arr[e]:  # 시작문자 == 끝문자인 경우
            if s == e-1:    # 길이가 2면 펠린드롬
                dp[s][e] = 1
            elif dp[s+1][e-1] == 1: # 안쪽이 펠린드롬이라면
                dp[s][e] = 1

for _ in range(M):
    S,E = map(int,input().split())
    print(dp[S-1][E-1])