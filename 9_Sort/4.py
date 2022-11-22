def sortAlphabet(lst):
    sort_lst = []
    for i in lst:
        for j in i:
            if j.isalpha():
                sort_lst.append([i,j])

    for i in range(len(sort_lst)):
        for j in range(len(sort_lst)-1):
            if sort_lst[j][1] > sort_lst[j+1][1]:
                sort_lst[j], sort_lst[j+1] = sort_lst[j+1], sort_lst[j]
    
    return sort_lst

inp = input('Enter Input : ').split()
sorted_inp = sortAlphabet(inp)
for i in sorted_inp:
    print(i[0], end=' ')