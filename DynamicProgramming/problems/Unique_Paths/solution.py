

# Just recursion
def allUniquePaths(i, j):
    if(i>m or j>n):
        return 0
    if(i==m and j==n):
        return 1
    return allUniquePaths(i+1, j) + allUniquePaths(i, j+1)
m, n = map(int, input("Enter values : ").split())
print(f'Unique paths = {allUniquePaths(1, 1)}')
# Time: O(N^(row*col)), Space:O(M + N)

# Top - down approach (memoization technique)
def allUniquePaths(i, j):
    if(i>m or j>n):
        return 0
    if(i==m and j==n):
        return 1
    if(dp[i][j] != -1):
        return dp[i][j]
    dp[i][j] = allUniquePaths(i+1, j) + allUniquePaths(i, j+1)
    return dp[i][j]
m, n = map(int, input("Enter values : ").split())
dp = [[-1 for i in range(n+1)] for i in range(m+1)]
print(f'Unique paths = {allUniquePaths(1, 1)}')
# Time: O(M * N), Space:O(M * N)

# Bottom - up approach (Tabulation technique)
def allUniquePaths():
    for i in range(m):
        for j in range(n):
            if(i==0 or j==0):
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[m-1][n-1]
m, n = map(int, input("Enter values : ").split())
dp = [[-1 for i in range(n+1)] for i in range(m+1)]
print(f'Unique paths = {allUniquePaths()}')
# Time: O(M * N), Space:O(M * N)

# Without extra space
def allUniquePaths():
    for i in range(m):
        curArr = [0 for i in range(n)]
        for j in range(n):
            if(i==0 or j==0):
                curArr[j] = 1
            else:
                curArr[j] = prevArr[j] + curArr[j-1]
        prevArr = curArr.copy()
    return prevArr[n-1]
m, n = map(int, input("Enter values : ").split())
prevArr = [0 for i in range(n+1)]
print(f'Unique paths = {allUniquePaths()}')
# Time: O(M * N), Space:O(N)

