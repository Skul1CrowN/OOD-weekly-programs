def decToBin(n: int):
    if n == 0:
        return 0
    else:
        return (n % 2 + 10 * int(decToBin(n // 2)))

def power(max: int, n = 0):
    if max < 0:
        print('Only Positive & Zero Number ! ! !')
        return

    if n > 2**max - 1:
        return

    print(f"{decToBin(n):0{max}}")
    return power(max,n+1)

inp = int(input('Enter Number : '))
power(inp)
