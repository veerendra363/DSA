def subArraysXor(arr, x):
    hashTable = { }
    xr = 0
    count = 0
    for i in arr:
        xr ^= i
        temp = xr ^ x
        if(xr == x):
            count += 1
        if temp in hashTable:
            count += hashTable[temp]
        if xr not in hashTable:
            hashTable[xr] = 0
        hashTable[xr] += 1
    return count

n, x = map(int, input('Enter len and xor value : ').split())
arr = list(map(int, input('Enter values : ').split()))
print('No.of sub arrays : ', subArraysXor(arr, x))