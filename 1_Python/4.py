print("*** Fun with Drawing ***")
num = int(input("Enter input : "))
for i in range((num-1)*4+1):
    for j in range((num-1)*4+1):
        if i % 2 == 0 and j >= i and j <= (num-1)*4-i:
            print("#",end="")
        elif i % 2 == 0 and j <= i and j >= (num-1)*4-i:
            print("#",end="")
        elif i <= j and i >= (num-1)*4-j and j % 2 == 0:
            print("#",end="")
        elif i >= j and i <= (num-1)*4-j and j % 2 == 0:
            print("#",end="")
        else:
            print(".",end="")
    print("\n",end="")