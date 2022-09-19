def fibo(num):
    if num == 1:
        return 1
    elif num == 2:
        return 1
    return fibo(num-2) + fibo(num-1)

num_in = int(input("Enter Number : "))
print("fibo(" + str(num_in) + ") =", fibo(num_in))
