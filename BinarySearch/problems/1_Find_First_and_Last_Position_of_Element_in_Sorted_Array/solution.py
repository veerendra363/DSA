# Time complexity: O(log N), Space complexity: O(1)

def lowerBound(arr, target):
    low = 0
    high = len(arr) - 1
    while(low <= high):
        mid = (low + high) // 2
        if(arr[mid] < target):
            low = mid + 1
        else:
            high = mid - 1
    return low

def firstLastPositions(nums, target):
    numsLen = len(nums)
    if(numsLen == 0):
        return [-1, -1]
    firstPosition = lowerBound(nums, target)
    if(firstPosition >= 0 and firstPosition < numsLen and nums[firstPosition] == target):
        lastPosition = lowerBound(nums, target + 1) - 1
        return [firstPosition, lastPosition]
    return [-1, -1]

nums = list(map(int, list(input().split())))
target = int(input())
print(firstLastPositions(nums, target))

