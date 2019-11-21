from operation_class import Operation

x = float(input('Enter x : '))
y = float(input('Enter y : ')) 

op = Operation()
op.setX(x)
op.setY(y)

op.Show()
op.showResult(op.Addition())