class Calculator :

    def __init__(self, x):
        self.x = x

    def __add__(self, obj):
        return self.x + obj.x

    def __sub__(self, obj):

        return self.x - obj.x

    def __mul__(self, obj):

        return self.x * obj.x

    def __truediv__(self, obj):

        return self.x / obj.x

x,y = input("Enter num1 num2 : ").split(",")

x,y = Calculator(int(x)),Calculator(int(y))

print(x+y,x-y,x*y,x/y,sep = "\n")