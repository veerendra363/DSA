def lengthOfLongestSubstring(self, s: str) -> int:
    fixedPointer, movingPointer, hashTable, ans = 0, 0, {}, 0
    for ch in s:
        if ch not in hashTable:
            hashTable[ch] = -1
        if ch in hashTable and hashTable[ch] >= fixedPointer:
            ans = max(ans, movingPointer - fixedPointer)
            fixedPointer = hashTable[ch] + 1
        hashTable[ch] = movingPointer
        movingPointer += 1
    ans = max(ans, movingPointer - fixedPointer)
    return ans

string = input('Enter string :')
print('Len of longest sub-sting without repeating : ', lengthOfLongestSubstring(string))