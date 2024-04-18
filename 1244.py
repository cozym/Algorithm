# 스위치 켜고 끄기
import sys
input = sys.stdin.readline

N = int(input())
switch = list(map(int,input().split()))

def boy(num):
    for idx in range(num, N+1, num):
        switch[idx-1] = (1 if switch[idx-1]==0 else 0)

def girl(num):
    num -= 1
    step = 1
    switch[num] = (1 if switch[num]==0 else 0)
    while True:
        if num-step < 0 or num+step >= N or switch[num-step] != switch[num+step]:
            break
        switch[num-step] = (1 if switch[num-step]==0 else 0)
        switch[num+step] = (1 if switch[num+step]==0 else 0)
        step += 1

for _ in range(int(input())):
    gender,num = map(int,input().split())
    if gender == 1:
        boy(num)
    else:
        girl(num)

for p in range(N):
    if p != 0 and p%20==0:
        print()
    print(switch[p],end=' ')