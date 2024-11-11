# 카드 문자열
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    cards = list(input().split())

    q = []
    for card in cards:
        L = [card] + q
        R = q + [card]
        q = sorted([L,R])[0]

    print(''.join(q))