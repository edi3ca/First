def absolute (N):
    if N < 0:
        return -1 * N
    else:
        return N

print "|-1| = ", absolute(-1)
print "|100| =", absolute(100)
print "|0| =", absolute(0)


x=-9
if x<0:
    print 'Negative'
elif x==0:
    print 'Zero'
else:
    print 'Positive'

x=0
if x<0:
    print 'Negative'
elif x==0:
    print 'Zero'
else:
    'Positive'
#Tax ex.

def get_tax_amount(salary):
    if salary<20000:
        return 0
    elif salary>=20000 and salary< 50000:
        return salary*0.15
    elif salary>= 50000 and salary< 100000:
        return salary *0.20
    else:
        return salary * 0.33

print "Bob Tax - ", get_tax_amount(30000)
print "Jil Tax - ", get_tax_amount(45000)
print "Apu Tax - ", get_tax_amount(130000)
print "Tom Tax - ", get_tax_amount(17000)



