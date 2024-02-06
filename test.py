T = int(input())

res = 0

def recursion(ability,team,pointer,k,ability_len):
    global res
    l = len(team)
    if pointer >= ability_len:
        if l > res:
            if abs(min(team)-max(team)) > k:
                res = l
        return
    team.append(ability[pointer])
    recursion(ability,team,pointer+1,k,ability_len)
    team.pop()
    recursion(ability,team,pointer+1,k,ability_len)

for test_case in range(1, T + 1):
    res = []
    team = []
    N,K = map(int,input().split())
    ability= list(map(int,input().split()))
    dp = [[0,0,0] for i in range(len(ability))]
    dp[0] = [1,ability[0],ability[0]]

    # dp[n][0] : n번째 사람을 포함하는 최대 인원
    # dp[n][1] : n번째 사람을 포함하는 최대 인원의 최솟값
    # dp[n][2] : n번째 사람을 포함하는 최대 인원의 최댓값
    for i in range(1,len(ability)):
        for j in range(0,i+1):
            if dp[i][0] < dp[j][0]+1:
                if abs(ability[j] - dp[i][1]) > K and abs(dp[i][2] - ability[j]) > K:
                    dp[i][0] = dp[j][0]+1
                    dp[i][1] = dp[j][1]
                    dp[i][2] = dp[j][2]
                    res.append(dp[i][0])
    print("#{} {}" .format(test_case,max(res)))