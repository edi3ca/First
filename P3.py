
#Find Hypotenuse using Pythagoras
from math import sqrt


def find_hypotenuse(a,b):
    a_sqrt = a*a
    b_sqrt = b*b
    leg_sum= a_sqrt + b_sqrt
    return sqrt(leg_sum)

leg1 = 2.00
leg2 = 5.00

hypotenuse = find_hypotenuse(leg1, leg2)
print "a =", leg1
print "b =", leg2

print hypotenuse
print find_hypotenuse(2.0, 3.0)
print find_hypotenuse(3, 4)

def print_name(name):
    print 'Person name >>>>> ' + name

print_name('Elma ')
print_name('Canon ')
print_name('Moreno')
