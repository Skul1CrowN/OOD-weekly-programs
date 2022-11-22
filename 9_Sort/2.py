def findMax(lis, index=0):
    if index == len(lis)-1:
        return index
    k = findMax(lis, index+1)
    return index if lis[index] > lis[k] else k

def selSort(lis, stop):
    if stop == 0:
        return
    nowLis = lis.copy()
    mxIndex = findMax(nowLis[:stop+1])
    mx = lis[mxIndex]
    if mxIndex != stop:
        temp = lis[stop]
        lis[mxIndex] = lis[stop]
        lis[stop] = mx
        print('swap {0} <-> {1} :'.format(temp, mx), str(lis))
    selSort(lis, stop-1)

inp = list(map(int,input("Enter Input : ").split()))
temp = inp.copy()
selSort(temp, len(temp)-1)
print(temp)
