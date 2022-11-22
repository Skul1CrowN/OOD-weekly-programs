def findPlace(lst,val,index=0):
    if index == len(lst) or lst[index]>=val:
        return index
    return findPlace(lst,val,index+1)

def insertionSort(init,lst,index=0):
    if len(lst)==0:
        return init

    placeIndex=findPlace(init,lst[index])

    if placeIndex == -1:
        temp=[]
        temp.append(lst[index])
        init=temp+init
        num=lst.pop(0)
        print('insert {0} at index {1} : '.format(num,0)+str(init),end='')
        if len(lst)!=0:
            print(' '+str(lst))
        else:
            print('')

    elif placeIndex == len(init):
        init.append(lst[index])
        num=lst.pop(0)
        print('insert {0} at index {1} : '.format(num,len(init)-1)+str(init),end='')
        if len(lst)!=0:
            print(' '+str(lst))
        else:
            print('')
    else:
        temp1=init[:placeIndex]
        temp2=init[placeIndex:]
        temp3=[]
        temp3.append(lst[index])
        init=temp1+temp3+temp2
        num=lst.pop(0)
        print('insert {0} at index {1} : '.format(num,placeIndex)+str(init),end='')
        if len(lst)!=0:
            print(' '+str(lst))
        else:
            print('')
    
    return insertionSort(init,lst)

inp = list(map(int,input("Enter Input : ").split()))
sorted_list=insertionSort(inp[0:1],inp[1:])

print('sorted')
print(sorted_list)