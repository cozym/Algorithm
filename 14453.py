# Hoof, Paper, Scissors (Silver)
# H > S , S > P , P > H
import sys
input = sys.stdin.readline

N = int(input())
H = [0]*(N+1)
S = [0]*(N+1)
P = [0]*(N+1)
res = 0
# H -> S , P
# S -> H , P
# P -> H , S
# 로 바꾸는 모든 경우 고려

for i in range(1,N+1):
    FJ = input().rstrip()
    H[i] = H[i-1]
    S[i] = S[i-1]
    P[i] = P[i-1]
    if FJ == 'H':
        H[i] += 1
    elif FJ == 'S':
        S[i] += 1
    elif FJ == 'P':
        P[i] += 1

for i in range(1,N+1):
    res = max(S[i] + P[N]-P[i],    # H를 내다가 S로 바꾸는 경우
                S[i] + H[N]-H[i],    # H를 내다가 P로 바꾸는 경우
                H[i] + S[N]-S[i],
                H[i] + P[N]-P[i],
                P[i] + H[N]-H[i],
                P[i] + S[N]-S[i], res)

print(res)