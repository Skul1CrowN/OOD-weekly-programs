def odd_even(arr, s):
    list = []
    if s == "Odd":
        for i in range(len(arr)):
            if(i+1)%2 != 0:
                list.append(arr[i])
    else:
        for i in range(len(arr)):
            if(i+1)%2 == 0:
                list.append(arr[i])
    return list


print("*** Odd Even ***")
type, arr, s = input("Enter Input : ").split(',')
if type == 'S':
    temp = list(arr)
else:
    temp = list(arr.split(" "))
ans = odd_even(temp,s)
if type == 'S':
    print(''.join(str(i) for i in ans))
else:
    print(ans)