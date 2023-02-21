# Just recursion
def maxProfit(i, w):
    if(i == 0):
        if(arr[0][i] <= w):
           return arr[1][i]
        return 0
    pick = 0
    if(arr[0][i] <= w):
        pick = arr[1][i] + maxProfit(i-1, w - arr[0][i])
    notPick = maxProfit(i-1, w)
    return max(pick, notPick)

n = int(input('Enter number : '))
arr = []
for j in range(2):
    arr.append(list(map(int, input('Enter Data : ').split())))
w = int(input('Enter weight : '))
print(f'Max Profit : {maxProfit(n-1, w)}')
#Time O(2^N), Space: O(N)

# Top - down approach (memoization technique)
def maxProfit(i, w):
    if(i == 0):
        if(arr[0][i] <= w):
            return arr[1][i]
        return 0
    if(dp[i][w] != -1):
        return dp[i][w]
    pick = 0
    if(arr[0][i] <= w):
        pick = arr[1][i] + maxProfit(i-1, w - arr[0][i])
    notPick = maxProfit(i-1, w)
    dp[i][w] = max(pick, notPick)
    return dp[i][w]

n = int(input('Enter number : '))
arr = []
for j in range(2):
    arr.append(list(map(int, input('Enter Data : ').split())))
w = int(input('Enter weight : '))
dp = [[-1 for i in range(w+1)] for j in range(n)]
print(f'Max Profit : {maxProfit(n-1, w)}')
# Time: O(n * w) Space: O(n * w)

# Bottom - up approach (Tabulation technique)
n = int(input('Enter number : '))
arr = []
for i in range(2):
    arr.append(list(map(int, input('Enter Data : ').split())))
w = int(input('Enter weight : '))
dp = [[0 for m in range(w+1)] for j in range(n)]
for m in range(arr[0][0], w+1):
    dp[0][m] = arr[1][0]
for k in range(1, n):
    for l in range(w+1):
        p = 0
        if(arr[0][k] <= l):
            p = arr[1][k] + dp[k-1][l - arr[0][k]]
        np = dp[k-1][l]
        dp[k][l] = max(p, np)
print(f'Max Profit- : {dp[n-1][w]}')
# Time: O(n * w) space:O(n * w)

# Without extra space
n = int(input('Enter number : '))
arr = []
for j in range(2):
    arr.append(list(map(int, input('Enter Data : ').split())))
w = int(input('Enter weight : '))
dp = [0 for m in range(w+1)]
for m in range(arr[0][0], w+1):
    dp[m] = arr[1][0]
for k in range(1, n):
    temp = [0 for m in range(w+1)]
    for l in range(w+1):
        p = 0
        if(arr[0][k] <= l):
            p = arr[1][k] + dp[l - arr[0][k]]
        np = dp[l]
        temp[l] = max(p, np)
    dp = temp.copy()
print(f'Max Profit : {dp[w]}')
# Time:O(n * w) space: O(w)