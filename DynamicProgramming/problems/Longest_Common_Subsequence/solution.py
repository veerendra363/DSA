# Just recursion
def lcs(i1, i2):
	if(i1 < 0 or i2 < 0):
		return 0
	if(s[i1] == t[i2]):
		return 1 + lcs(i1 - 1, i2 - 1)
	return max(lcs(i1 - 1, i2), lcs(i1, i2 - 1))

s = input('Enter String 1 : ')
t = input('Enter String 2 : ')
n = len(s)
m = len(t)
print(f'LCS length = {lcs(n-1, m-1)}')
#Time O(2^(N+M)), Space: O(N+M)


# Top - down approach (memoization technique)
def lcs(i1, i2):
    if(i1 < 0 or i2 < 0):
        return 0
    if(s[i1] == t[i2]):
        return 1 + lcs(i1 - 1, i2 - 1)
    if(dp[i1][i2] != -1):
        return dp[i1][i2]
    dp[i1][i2] = max(lcs(i1 - 1, i2), lcs(i1, i2 - 1))
    return dp[i1][i2]

s = input('Enter String 1 : ')
t = input('Enter String 2 : ')
n = len(s)
m = len(t)
dp = [[-1 for i in range(m+1)] for j in range(n+1)]
print(f'LCS length = {lcs(n-1, m-1)}')
#Time: O(N+M), Space: O(N*M) 

# Bottom - up approach (Tabulation technique)
s = input('Enter String 1 : ')
t = input('Enter String 2 : ')
n = len(s)
m = len(t)
dp = [[0 for i in range(m+1)]for j in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        if(s[i-1] == t[j-1]):
            dp[i][j] = 1 + dp[i-1][j-1]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(f'LCS length : {dp[n][m]}')
#Time: O(N+M), Space: O(N*M) 

# Without extra space
s = input('Enter String 1 : ')
t = input('Enter String 2 : ')
n = len(s)
m = len(t)
dp = [0 for i in range(m+1)]
for i in range(1, n+1):
    curr = [0 for i in range(m+1)]
    for j in range(1, m+1):
        if(s[i-1] == t[j-1]):
            curr[j] = 1 + dp[j-1]
        else:
            curr[j] = max(dp[j], curr[j-1])
    dp = curr.copy()
print(f'LCS length = {dp[m]}')
#Time: O(N+M), Space: O(M) 
