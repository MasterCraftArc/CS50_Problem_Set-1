equation = input('enter the equation: ')

a = equation.split(' ')

x,y,z = a[0],a[1],a[2]

if y == '+' :
    print(float(x)+float(z))
elif y == '-' :
    print (float(x) - float(z))
elif y == '*':
    print (float(x)*float(z))
elif y == '/':
    print (float(x)/float(z))
