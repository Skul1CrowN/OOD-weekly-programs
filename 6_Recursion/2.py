def maxIndex(arr,i,j):
    if i == j:
        return i
    
    k = maxIndex(arr,i+1,j)

    return (i if arr[i] > arr[k] else k)

def recursiveSort(a,n,index = 0):
    if index == n:
        return -1
    
    k = maxIndex(a,index,n-1)

    if k != index:
        a[k], a[index] = a[index], a[k]

    recursiveSort(a,n,index+1)

inp = list(map(int, input("Enter your List : ").split(',')))
recursiveSort(inp,len(inp))
print("List after Sorted :",inp)