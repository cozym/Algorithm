# 방 배정하기
import sys
input = sys.stdin.readline

A,B,C,N = map(int,input().split())

def room():
    for a in range(0,N+1,A):
        for b in range(0,N+1,B):
            for c in range(0,N+1,C):
                if a+b+c == N:
                    return 1
    else:
        return 0

print(room())