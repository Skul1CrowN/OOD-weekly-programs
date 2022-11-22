def searchFGV(l, r, arr, x):
    mid = l + (r - l) // 2
    if l == r:
        if r == len(arr) - 1:
            return 'No First Greater Value'
        else:
            return str(arr[mid])
    
    if arr[mid] <= x:
        l = mid + 1
    elif arr[mid] > x:
        r = mid

    return searchFGV(l,r,arr,x)

inp1, inp2 = input('Enter Input : ').split('/')
inp1, inp2 = list(map(int, inp1.split())), list(map(int, inp2.split()))
for i in inp2:
    print(searchFGV(0, len(inp1) - 1, sorted(inp1), i))