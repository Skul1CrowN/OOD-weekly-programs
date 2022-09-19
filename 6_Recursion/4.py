def pantip(k, n, arr, path):
    possible = 0
    if arr == []:
        return
    
    if n+arr[0] > k:
        pan = pantip(k,n,arr[1:],path)
        if pan is not None:
            possible += pan

    elif n+arr[0] < k:
        path.append(arr[0])
        pan = pantip(k,n+arr[0],arr[1:],path)
        if pan is not None:
            possible += pan
        path.pop()
        pan = pantip(k,n,arr[1:],path)
        if pan is not None:
            possible += pan
    
    elif n+arr[0] == k:
        path.append(arr[0])
        possible += 1
        print(str(path).replace('[','').replace(']','').replace(',',''))
        path.pop()
        pan = pantip(k,n,arr[1:],path)
        if pan is not None:
            possible += pan
        return possible

    return possible


inp = input('Enter Input (Money, Product) : ').split('/')
arr = [int(i) for i in inp[1].split()]
pattern = pantip(int(inp[0]), 0, arr, [])
print("Krisada can purchase Product: {0} with: {1} Baht | {2} Pattern".format(arr, inp[0], pattern))