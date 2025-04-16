# 문자열 게임 2
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    dic = {}
    s = input().rstrip()
    k = int(input())

    shortest = 10001
    longest = 0
    for i in range(len(s)):
        if s[i] not in dic:
            dic[s[i]] = []
        dic[s[i]].append(i)
        if len(dic[s[i]]) >= k:
            cur = dic[s[i]][-1] - dic[s[i]][-k] + 1
            shortest = min(shortest, cur)
            longest = max(longest, cur)
    
    if longest == 0:
        print(-1)
    else:
        print(shortest, longest)