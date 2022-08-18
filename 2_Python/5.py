class Torkam:
    def __init__(self, enter):
        self.ls, oper, text, enter = [], "", "", enter.split(",")
        for i in range(len(enter)):
            if ' ' in enter[i]:
                oper, text = enter[i].split(" ")[0], enter[i].split(" ")[1]
            else:
                oper = enter[i]

            if oper == 'P':
                self.play(text)
            elif oper == 'R':
                self.restart()
            elif oper == 'X':
                exit(0)
            else:
                print(f'\'{enter[i]}\' is Invalid Input !!!')
                exit(0)

    def play(self, text):
        if len(self.ls) == 0:
            self.ls.append(text)
            print(f'\'{text}\' -> { self.ls}')

        elif self.ls[-1][-2:].lower() == text[:2].lower():
            self.ls.append(text)
            print(f'\'{text}\' -> { self.ls}')

        else:
            print(f'\'{text}\' -> game over')

    def restart(self):
        self.ls.clear()
        print("game restarted")

print("*** TorKham HanSaa ***")
torkam = Torkam(input("Enter Input : "))
