arr = list(map(int, input().split()))

sm = second_sm = float('inf')
lg = second_lg = float('-inf')

for i in arr:
    if i < sm:
        second_sm = sm
        sm = i
    elif i < second_sm:
        second_sm = i

for i in arr:
    if i > lg:
        second_lg = lg
        lg = i
    elif i < second_lg:
        second_lg = i
        
print("second smallest element is {} and second largest element is {}".format(second_sm, second_lg))
