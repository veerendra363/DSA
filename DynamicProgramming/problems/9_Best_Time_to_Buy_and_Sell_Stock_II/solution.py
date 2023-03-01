# Top - down approach (memoization technique)
def maxProfit(i, buy):
    if(i == n):
        return 0
    if(dp[i][buy] != -1):
        return dp[i][buy]
    if(buy):
        dp[i][buy] = max(-prices[i] + maxProfit(i+1, 0), maxProfit(i+1, 1))
    else:
        dp[i][buy] = max(prices[i] + maxProfit(i+1, 1), maxProfit(i+1, 0))
    return dp[i][buy]

n = int(input('Enter size : '))
prices = list(map(int, input('Enter Prices : ').split()))
dp = [[-1 for i in range(2)]for j in range(n)]
print(f'Max Profit = {maxProfit(0, 1)}')
#Time: O(N*N), Space:O(N)

# Bottom - up approach (Tabulation technique) - Space optimized
n = int(input('Enter size : '))
prices = list(map(int, input('Enter Prices : ').split()))
dp = [0, 0]
for i in range(n-1, -1, -1):
    dp[0] = max(prices[i] + dp[1], dp[0])
    dp[1] = max(-prices[i] + dp[0], dp[1])
print(f'Max Profit = {dp[1]}')
#Time: O(N), Space:O(1)
