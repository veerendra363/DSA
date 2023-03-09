# Iteration Method
def ibs(arr, k):
    low = 0
    high = len(arr) - 1
    while(low <= high):
        mid = (low + high) // 2
        if(arr[mid] == k):
            return True
        if(k > arr[mid]):
            low = mid + 1
        else:
            high = mid - 1
    return False

arr = list(map(int, input('Enter values : ').split()))
k = int(input('Enter value : '))
print(ibs(arr, k))

#Recursive Method
def rbs(arr, k, low, high):
    if(low > high):
        return False
    mid = (low + high) // 2
    if(arr[mid] == k):
        return True
    if(k > arr[mid]):
        return rbs(arr, k, mid+1, high)
    return rbs(arr, k, low, mid - 1)

arr = list(map(int, input('Enter values : ').split()))
k = int(input('Enter value : '))
print(rbs(arr, k, 0, len(arr) - 1))