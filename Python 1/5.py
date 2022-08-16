num = int(input("Enter Input : "))
for i in range(int((4+2*num)/2)):
    for j in range(int((4+2*num)/2)):
        if int((4+2*num)/2)-i-1 > j:
            print(".", end="")
        else:
            print("#", end="")
    for j in range(int((4+2*num)/2)):
        if i == 0 or i == int((4+2*num)/2)-1 or j == 0 or j == int((4+2*num)/2)-1:
            print("+", end="")
        else:
            print("#", end="")
    print("\n",end="")
for i in range(int((4+2*num)/2)):
    for j in range(int((4+2*num)/2)):
        if i == 0 or i == int((4+2*num)/2)-1 or j == 0 or j == int((4+2*num)/2)-1:
            print("#", end="")
        else:
            print("+", end="")
    for j in range(int((4+2*num)/2)):
        if int((4+2*num)/2)-i > j:
            print("+", end="")
        else:
            print(".", end="")
    print("\n",end="")