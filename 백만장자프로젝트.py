# SW Expert Academy .1859
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    prices = list(map(int,input().split()))
    res = 0
    while len(prices) != 0:
        m = max(prices)
        beforeMax = prices[:prices.index(m)+1]
        res += (len(beforeMax)-1)*beforeMax[-1]-(sum(beforeMax)-beforeMax[-1])
        if len(prices)==len(beforeMax):
            break
        prices = prices[prices.index(m)+1:]
    print("#{} {}".format(test_case, res))
