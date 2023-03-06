## Top - down approach (memoization technique)
from math import *

def mcm(i, j):
    if(i == j or i > j):
        return 0
    if(dp[i][j] != -1):
        return dp[i][j]
    ans = inf
    for k in range(i, j):
        ans = min(ans, arr[i-1] * arr[k] * arr[j] + mcm(i, k) + mcm(k+1, j))
    dp[i][j] =  ans
    return dp[i][j]

n = int(input('Enter length : '))
arr = list(map(int, input('Enter dimensions : ').split()))
dp = [[-1 for i in range(n)]for j in range(n)]
print(f'MCM : {mcm(1, n-1)}')
#Time: O(N^3), Space: O(N^2 + N)

# Bottom - up approach (Tabulation technique)
from math import *

n = int(input('Enter length : '))
arr = list(map(int, input('Enter dimensions : ').split()))
dp = [[0 for i in range(n)]for j in range(n)]

for i in range(n-1, 0, -1):
    for j in range(i+1, n):
        ans = inf
        for k in range(i, j):
            ans = min(ans, arr[i-1] * arr[k] * arr[j] + dp[i][k] + dp[k+1][j])
        dp[i][j] = ans 

print(f'MCM : {dp[1][n-1]}')
#Time: O(N^3), Space: O(N^2)

