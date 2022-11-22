def bubbleSort(l):
    if len(l) <= 1:
        return l
    if len(l) == 2:
        return l if l[0] < l[1] else [l[1], l[0]]
    
    left = l[2:]
    res = []
    if l[0] < l[1]:
        res = [l[0]] + bubbleSort([l[1]] + left)
    else:
        res = [l[1]] + bubbleSort([l[0]] + left)

    return bubbleSort(res[:-1]) + res[-1:]

inp = list(map(int, input('Enter Input : ').split()))
print(bubbleSort(inp))