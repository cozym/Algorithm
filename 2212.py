# 센서
import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
sensors = list(map(int,input().split()))
distance = []

sensors.sort()
for idx in range(1,N):
    distance.append(sensors[idx]-sensors[idx-1])

distance.sort()

for _ in range(K-1):
    distance.pop()

print(sum(distance))