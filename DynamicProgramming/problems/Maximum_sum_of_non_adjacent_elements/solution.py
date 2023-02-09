# Recurrence Relation
# pick = arr[i] + maxSum(i-2)
# notPick = maxSum(i-1)

# Just recursion
def maxSum(i):
    if(i < 0):
        return 0
    pick = arr[i] + maxSum(i-2)
    notPick = maxSum(i-1)
    return max(pick, notPick)
n = int(input("Enter number : "))
arr = list(map(int, input("Enter values : ").split()))
print(f'max sum = {maxSum(n-1)}')
# Time: O(2^n) Space: O(n)

# Top - down approach (memoization technique)
def maxSum(i):
    if(i < 0):
        return 0
    if(dp[i] == -1):
        pick = arr[i] + maxSum(i-2)
        notPick = maxSum(i-1)
        dp[i] = max(pick, notPick)
    return dp[i]
n = int(input("Enter number : "))
arr = list(map(int, input("Enter values : ").split()))
dp = [-1 for i in range(n)]
print(f'max sum = {maxSum(n-1)}')
# Time: O(n) Space: O(n)

# Bottom - up approach (Tabulation technique)
def maxSum(n):
    if(n <= 0):
        return 0
    if(n == 1):
        return arr[0]
    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])
    for i in range(2, n):
        pick = arr[i] + dp[i-2]
        notPick = dp[i-1]
        dp[i] = max(pick, notPick)
    return dp[n-1]
n = int(input("Enter number : "))
arr = list(map(int, input("Enter values : ").split()))
dp = [-1 for i in range(n)]
print(f'max sum = {maxSum(n)}')
# Time: O(n) space:O(n)

# Without extra space
def maxSum(n):
    if(n <= 0):
        return 0
    if(n == 1):
        return arr[0]
    p2 = arr[0]
    p1 = max(arr[0], arr[1])
    for i in range(2, n):
        curr = arr[i] + p2
        p2 = p1
        p1 = max(p2, curr)
    return p1
n = int(input("Enter number : "))
arr = list(map(int, input("Enter values : ").split()))
print(f'max sum = {maxSum(n)}')
# Time:O(n) space: O(1)