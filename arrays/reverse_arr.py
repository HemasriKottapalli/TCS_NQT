arr = list(map(int, input().split()))

reversed_arr = []

for i in range(len(arr)-1, -1, -1):
    reversed_arr.append(arr[i])
    
print(arr, reversed_arr)
