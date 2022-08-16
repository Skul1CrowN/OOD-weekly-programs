print("*** Election ***")
n = int(input("Enter a number of voter(s) : "))
score = [0]*20
temp = list(map(int, list(input().split(' '))))
for i in range(n):
    if(temp[i] >= 1 and temp[i] <= 20):
        score[temp[i]-1] += 1
max = 0
winner = []
for i in range(len(score)):
    if score[i] > max:
        winner.clear()
        winner.append(i+1)
        max = score[i]
    elif score[i] == max and max != 0:
        winner.append(i+1)

if(winner == []):
    print("*** No Candidate Wins ***")
else:
    for i in range(len(winner)):
        if i < len(winner)-1:
            print(winner[i], end=" ")
        else:
            print(winner[i], end="")