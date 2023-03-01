# https://www.youtube.com/watch?v=AxNNVECce8c&list=PLgUwDviBIf0rGlzIn_7rsaR2FQ5e6ZOL9
# print all subsequences

#Pick not pick method
def getAllSubsequences(i, arr):
    if(i == n):
        print(arr, end=", ")
        return
    # pick index i
    getAllSubsequences(i+1, arr + [values[i]])

    #not pick index i
    getAllSubsequences(i+1, arr)

n = int(input("Enter number : "))
print("Enter values : ", end="")
values = list(map(int, input().split()))
print('All subsequences are :- ')
getAllSubsequences(0, [])
#time: O(2^n) space:O(N^2)