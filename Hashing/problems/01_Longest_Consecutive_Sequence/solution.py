def longestConsecutive(nums):
    ans = 0
    htable = {}
    for i in nums:
        htable[i] = 1
    for i in nums:
        count = 1
        if((i-1) not in htable):
            while((i + count) in htable):
                count += 1
        ans = max(count, ans)
    return ans

nums = list(map(int, input().split()))
print('Longest consecutive sequence length :', longestConsecutive(nums))