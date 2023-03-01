# Just recursion
def minPath(r, i):
    if(r >= n):
        return 0 
    return arr[r][i] + min(minPath(r+1, i), minPath(r+1, i+1))

n = int(input('Enter number : '))
arr = []
for i in range(n):
    arr.append(list(map(int, input(f'Enter Values of row-{i+1} : ').split())))
print(f'Min path value = {minPath(0, 0)}')
# Time: O(2^N), Space: O(N)

# Top - down approach (memoization technique)
def minPath(r, i):
    if(r >= n):
        return 0
    if(dp[r][i] == -1):
        dp[r][i] = arr[r][i] + min(minPath(r+1, i), minPath(r+1, i+1))
    return dp[r][i]

n = int(input('Enter number : '))
arr = []
for i in range(n):
    arr.append(list(map(int, input(f'Enter Values of row-{i+1} : ').split())))
dp = [[-1 for i in range(n)] for j in range(n)]
print(f'Min path value = {minPath(0, 0)}')
#Time: O(N^2), Space: O(N^2)

# Bottom - up approach (Tabulation technique)
def minPath(r, i):
    dp[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        for j in range(i+1):
            dp[i][j] = arr[i][j] + min(dp[i+1][j], dp[i+1][j+1])
    return dp[0][0]

n = int(input('Enter number : '))
arr = []
for i in range(n):
    arr.append(list(map(int, input(f'Enter Values of row-{i+1} : ').split())))
dp = [[-1 for i in range(n)] for j in range(n)]
print(f'Min path value = {minPath(0, 0)}')
# Time: O(N^2), Space: O(N^2)

# Without extra space
def minPath(r, i):
    dp = arr[n-1].copy()
    for i in range(n-2, -1, -1):
        for j in range(i+1):
            dp[j] = arr[i][j] + min(dp[j], dp[j+1])
    return dp[0]

n = int(input('Enter number : '))
arr = []
for i in range(n):
    arr.append(list(map(int, input(f'Enter Values of row-{i+1} : ').split())))
print(f'Min path value = {minPath(0, 0)}')
# Time: O(N^2), Space: O(N)