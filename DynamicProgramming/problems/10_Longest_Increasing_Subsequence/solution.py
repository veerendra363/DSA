# Top - down approach (memoization technique)
def lis(i, j):
    if(i == n):
        return 0
    if(dp[i][j+1] != -1):
        return dp[i][j+1]
    p = 0
    if(j==-1 or nums[j] < nums[i]):
        p = 1 + lis(i+1, i)
    np = lis(i+1, j)
    dp[i][j+1] = max(p, np)
    return dp[i][j+1]

n = int(input('Enter length : '))
nums = list(map(int, input('Enter numbers : ').split()))
dp=[[-1 for i in range(n)]for j in range(n+1)]
print(f'Longest increasing subsequences length = {lis(0, -1)}')
#Time: O(N^2) Space: O(N^2)

# Bottom - up approach (Tabulation technique)
n = int(input('Enter length : '))
nums = list(map(int, input('Enter numbers : ').split()))
dp = [0] * (n+1)
for i in range(n-1, -1, -1):
    cur = dp.copy()
    for j in range(i-1, -2, -1):
        p = 0
        if(j==-1 or nums[j] < nums[i]):
            p = 1 + dp[i+1]
        np = dp[j+1]
        cur[j+1] = max(p, np)
    dp = cur.copy()
print(f'Longest increasing subsequences length = {dp[0]}')

#------- or ----------

n = int(input('Enter length : '))
nums = list(map(int, input('Enter numbers : ').split()))
dp = [1] * n
for i in range(n-1, -1, -1):
    for j in range(i+1, n):
        if(nums[i] < nums[j]):
            dp[i] = max(dp[i], 1+dp[j])
print(f'Longest increasing subsequences length = {max(dp)}')
#Time: O(N^2) Space: O(N)

# Binary Search
def findPosition(arr, start, end, val):
    mid = 0
    while(start <= end):
        mid = (start + end) // 2
        if(val == arr[mid]):
            return mid 
        if(arr[mid] < val):
            start = mid + 1
        else:
            end = mid - 1
    return end + 1

n = int(input('Enter length : '))
nums = list(map(int, input('Enter numbers : ').split()))
temp = [nums[0]]
for i in nums:
    if i > temp[-1]:
        temp.append(i)
    else:
        pos = findPosition(temp, 0, len(temp) - 1, i)
        temp[pos] = i
print(f'Longest increasing subsequences length = {len(temp)}')
#Time: O(NlogN) Space: O(N)

