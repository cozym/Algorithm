# SW Expert Academy 1208.Flatten
for test_case in range(1, 11):
    N = int(input())
    heights = list(map(int,input().split()))

    for i in range(N):
        heights[heights.index(max(heights))] -= 1
        heights[heights.index(min(heights))] += 1
    print("#{} {}".format(test_case,max(heights)-min(heights)))
