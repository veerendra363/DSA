#Recurrence Relation
# misCost(i) = cost[i] + min(minsCost(i-1), minCost(i-2))

#Just recursion
def minCost(i):
    if(i == 0):
        return cost[i]
    if(i == -1):
        return 0
    return cost[i] + min(minCost(i-1), minCost(i-2))

n = int(input('Enter no.of stairs : '))
cost = []
for i in range(n):
    print(f'Enter cost of Stair-{i+1} : ',end="")
    cost.append(int(input()))
print(min(minCost(n - 1), minCost(n - 2)))
#time: O(2^n) splace: O(n)


#top - down approach (memoization technique)
def minCost(i):
    if(i == 0):
        return cost[i]
    if(i == -1):
        return 0
    if(dp[i] == -1):
        dp[i] =cost[i] + min(minCost(i-1), minCost(i-2))
    return dp[i]

n = int(input('Enter no.of stairs : '))
cost = []
for i in range(n):
    print(f'Enter cost of Stair-{i+1} : ',end="")
    cost.append(int(input()))
dp = [-1 for i in range(n+1)]
print(min(minCost(n - 1), minCost(n - 2)))
#time: O(n) space: O(n)

#Bottom - up approach (Tabulation technique)
def minCost():
    if(n == 1):
        return cost[0]
    if(n == 2):
        return min(cost[0], cost[1])
    dp = [cost[0], cost[1]]
    for i in range(2, n):
        dp.append(cost[i] + min(dp[i-1], dp[i-2]))
    return min(dp[n-1], dp[n-2])

n = int(input('Enter no.of stairs : '))
cost = []
for i in range(n):
    print(f'Enter cost of Stair-{i+1} : ',end="")
    cost.append(int(input()))
print(minCost())
#time: O(n) space: O(n)

#Without extra space
def minCost():
    if(n == 1):
        return cost[0]
    if(n == 2):
        return min(cost[0], cost[1])
    p = cost[0]
    q = cost[1]
    for i in range(2, n):
        curr = cost[i] + min(p, q)
        p = q
        q = curr
    return min(p, q)

n = int(input('Enter no.of stairs : '))
cost = []
for i in range(n):
    print(f'Enter cost of Stair-{i+1} : ',end="")
    cost.append(int(input()))
print(minCost())
#time: O(n) space: O(1)

    

    