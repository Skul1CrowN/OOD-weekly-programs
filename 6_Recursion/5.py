def asteroid_collision(asts,i):
    if i == -1:
        return asts
    
    temp = asteroid_collision(asts,i-1)
    currentAst = temp[i]
    if currentAst > 0 and i < len(temp) - 1:
        nextAst = temp[i+1]
        if nextAst < 0:
            if abs(nextAst) < currentAst:
                temp[i+1] = currentAst
                temp[i] = 0
                temp = asteroid_collision(temp,i+1)
            elif abs(nextAst) > currentAst:
                temp[i] = nextAst
                temp[i+1] = 0
                temp = asteroid_collision(temp,i+1)
            else:
                temp[i] = 0
                temp[i+1] = 0
        if nextAst == 0:
            temp[i+1] = currentAst
            temp[i] = 0
            temp = asteroid_collision(temp,i+1)
    if currentAst < 0 and i > 0:
        nextAst = temp[i-1]
        if nextAst > 0:
            if abs(currentAst) < nextAst:
                temp[i] = nextAst
                temp[i-1] = 0
                temp = asteroid_collision(temp,i)
            elif abs(currentAst) > nextAst:
                temp[i-1] = currentAst
                temp[i] = 0
                temp = asteroid_collision(temp,i-1)
            else:
                temp[i] = 0
                temp[i-1] = 0
        if nextAst == 0:
            temp[i-1] = currentAst
            temp[i] = 0
            temp = asteroid_collision(temp,i-1)

    return temp

x = input("Enter Input : ").split(",")
x = list(map(int,x))
print([i for i in asteroid_collision(x, len(x) - 1) if i != 0])
