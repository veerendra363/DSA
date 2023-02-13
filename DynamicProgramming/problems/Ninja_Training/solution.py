
# Just recursion
def maxPoints(day, last):
    maxVal = 0
    if(day == 0):
        for i in range(3):
            if(i != last):
                maxVal = max(maxVal, points[day][i])
        return maxVal
    for i in range(3):
        if(i != last):
            maxVal = max(maxVal, points[day][i] + maxPoints(day - 1, i))
    return maxVal
n = int(input("Enter number: "))
points = []
for i in range(n):
    arr = list(map(int, input(f'Enter day-{i+1} Points : ').split()))
    points.append(arr)
print(f'Max Points = {maxPoints(n-1, 3)}')
#Time: O(N^2), Space: O(N)

# Top - down approach (memoization technique)
def maxPoints(day, last):
    if(dp[day][last] != -1):
        return dp[day][last]
    maxVal = 0
    if(day == 0):
        for i in range(3):
            if(i != last):
                maxVal = max(maxVal, points[day][i])
        return maxVal
    for i in range(3):
        if(i != last):
            maxVal = max(maxVal, points[day][i] + maxPoints(day - 1, i))
    dp[day][last] = maxVal
    return maxVal
n = int(input("Enter number: "))
points = []
for i in range(n):
    arr = list(map(int, input(f'Enter day-{i+1} Points : ').split()))
    points.append(arr)
dp = [[-1, -1, -1, -1] for i in range(n)]
print(f'Max Points = {maxPoints(n-1, 3)}')
# Time: O(N), Space: O(N)

# Bottom - up approach (Tabulation technique)
def maxPoints(day):
    for i in range(3):
        dp[day][i] = points[day][i]
    for d in range(day-1, -1, -1):
        for i in range(3):
            maxVal = 0
            for j in range(3):
                if(i != j):
                    maxVal = max(maxVal, points[d][i] + dp[d+1][j])
            dp[d][i] = maxVal
    return max(dp[0])
n = int(input("Enter number: "))
points = []
for i in range(n):
    arr = list(map(int, input(f'Enter day-{i+1} Points : ').split()))
    points.append(arr)
dp = [[-1, -1, -1, -1] for i in range(n)]
print(f'Max Points -= {maxPoints(n-1)}')
# Time: O(N), Space: O(N)

# Without extra space
def maxPoints(day):
    ans = points[day]
    for d in range(day-1, -1, -1):
        temp = [-1, -1, -1]
        for  i in range(3):
            maxVal = 0
            for j in range(3):
                if(i != j):
                    maxVal = max(maxVal, points[d][i] + ans[j])
            temp[i] = maxVal
        ans = temp.copy()
    return max(ans)

n = int(input("Enter number: "))
points = []
for i in range(n):
    arr = list(map(int, input(f'Enter day-{i+1} Points : ').split()))
    points.append(arr)
print(f'Max Point= {maxPoints(n-1)}')
# Time: O(N), Space: O(1)