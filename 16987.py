# 계란으로 계란치기
import sys
input = sys.stdin.readline

N = int(input())
egg = []
state = [True for _ in range(N)]
res = 0
for _ in range(N):
    S,W = map(int,input().split())
    egg.append([S,W])

def recursion(idx, state, egg, dead):
    if idx >= N:
        global res
        res = max(res, dead)
        return
    if dead+(N-idx) < res:
        return
    if not state[idx] or state.count(True)==1:
        recursion(idx+1, state[:], egg[:], dead)
        return

    for i in range(N):
        if (not state[i]) or i == idx:
            continue
        crack = 0
        tmpEgg = [e[:] for e in egg]
        tmpState = state[:]

        tmpEgg[i][0] -= tmpEgg[idx][1]
        tmpEgg[idx][0] -= tmpEgg[i][1]
        
        if tmpEgg[i][0] < 1:
            tmpState[i] = False
            crack += 1
        if tmpEgg[idx][0] < 1:
            tmpState[idx] = False 
            crack += 1

        recursion(idx+1, tmpState[:], tmpEgg[:], dead+crack)

recursion(0, state[:], egg[:], 0)
print(res)