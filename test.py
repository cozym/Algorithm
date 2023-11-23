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
    res = 0
    team = []
    N,K = map(int,input().split())
    ability= list(map(int,input().split()))
    dp = [[0,0,0] for i in range(len(ability))]
    dp[0] = [ability[0],ability[0],ability[0]]

    # dp[n][0] : n번째 사람을 포함하는 최대 인원
    # dp[n][1] : n번째 사람을 포함하는 최대 인원의 최솟값
    # dp[n][2] : n번째 사람을 포함하는 최대 인원의 최댓값
    for i in range(len(ability)):
        dp


    recursion(ability,team,0,K,ability_len)

    print("#{} {}" .format(test_case,res))