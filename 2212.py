# 센서
import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
sensors = list(map(int,input().split()))
distance = []

sensors.sort()
for idx in range(N-1):
    distance.append(sensors[idx+1]-sensors[idx])

distance.sort()

for _ in range(K-1):
    if distance:
        distance.pop()

print(sum(distance))