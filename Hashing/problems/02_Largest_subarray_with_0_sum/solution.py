def maxLen(arr):
    hashTable = {}
    s = 0
    ans = 0
    for i, val in enumerate(arr):
        s += val
        if(s == 0):
            ans = i + 1
            continue
        if(s in hashTable):
            ans = max(ans, i - hashTable[s])
        else:
            hashTable[s] = i
    return ans

arr = list(map(int, input('Enter values :').split()))
print('Length of the largest sub array : ', maxLen(arr))