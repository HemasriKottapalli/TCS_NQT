arr = list(map(int, input().split()))

minimum = arr[0]   # initialize with first element

for i in arr:
    if i < minimum:
        minimum = i

print(minimum)
