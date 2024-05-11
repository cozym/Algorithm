T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    farm = []
    for i in range(N):
        line = input()
        farm.append([])
        for j in line:
            farm[i].append(int(j))
    res = 0

    end = 0
    mid = N // 2
    alpha = 1
    for x in range(N):
        if x == mid:
            alpha = -1
        res += sum(farm[x][mid-end : mid+end+1])
        end += alpha

    print("#{} {}".format(test_case,res))
    # ///////////////////////////////////////////////////////////////////////////////////