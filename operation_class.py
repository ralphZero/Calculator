class Operation:

    ''' def __init__(self, x, y):
        self.x = x
        self.y = y '''
    
    def __init__(self):
        self.x = 0
        self.y = 0
    
    def setY(self, y):
        self.y = y
    
    def setX(self, x):
        self.x = x

    def Addition(self):
        return self.x + self.y

    def Substraction(self):
        return self.x - self.y

    def Division(self):
        return self.x / self.y

    def Multiplication(self):
        return self.x * self.y
    
    def Show(self):
        print(f'The fisrt number is {self.x}, the second is {self.y}')
    
    def showResult(self, result):
        print(f'The result is : {result}')
