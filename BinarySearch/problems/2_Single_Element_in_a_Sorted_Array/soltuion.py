# Time complexity: O(log N), Space complexity: O(1)

def singleNonDuplicate(nums):
    if(len(nums) == 1):
        return nums[0]
    low = 0
    high = len(nums) - 2
    while(low <= high):
        # num >> 1 => num // 2
        mid = (low + high) >> 1

        # n ^ 1 = n + 1 if n is even
        # n ^ 1 = n - 1 if n is odd
        if(nums[mid] == nums[mid ^ 1]):
            low = mid + 1
        else:
            high = mid - 1
    return nums[low]

nums = list(map(int, input('Enter nums: ').split()))
print(singleNonDuplicate(nums))