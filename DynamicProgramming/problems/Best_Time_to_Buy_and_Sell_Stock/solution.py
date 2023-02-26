n = int(input('Enter size : '))
arr = list(map(int, input('Enter prices : ').split()))
mini = arr[0]
profit = 0
for i in arr:
    profit = max(profit, i - mini)
    mini = min(i, mini)
print(f'Max Profit = {profit}')




