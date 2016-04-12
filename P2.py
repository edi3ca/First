def cubic(x):
    result = x * x * x
    return result

def cubic2(x):
    return x * x * x


value1 = cubic(3)

value2 = cubic2(5)

print "Value 1 =", value1
print "Value 2 =", value2

def adder (n1, n2):
    return n1 + n2


print "Added = ", adder(5**2, 10)

def avg_three(n1, n2, n3):
    temp=n1+n2+n3
    return temp/3.0
print"Average = ", avg_three(18,19,23)
print "Average 2 = ", avg_three(15,15,15)
print "Average 3 = ", avg_three(30,30,30)
