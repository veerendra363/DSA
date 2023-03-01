# https://www.youtube.com/watch?v=69ZCDFy-OUo&list=PLgUwDviBIf0rGlzIn_7rsaR2FQ5e6ZOL9
# Sum of n natural numbers using recursion
# Example:
# n = 10 
# 55

#parameterized 
def sumOfNums(n, sum):
    if ( n==0 ):
        return sum
    return sumOfNums(n-1, n+sum)

n = int(input('Enter number : '))
s = sumOfNums(n, 0)
print(f'Sum of {n} numbers = {s}')
#Time: O(n) Space: O(n)

#functional recursion
def sumOfNums(n):
    if ( n==1 ):
        return 1
    return n + sumOfNums(n-1)

n = int(input('Enter number : '))
s = sumOfNums(n)
print(f'Sum of {n} numbers = {s}')
#Time: O(n) Space: O(n)