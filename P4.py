def pay_raise(current_salary):
    new_salary = 0
    if current_salary < 20000:
        new_salary = current_salary * 1.10
    else:
        new_salary = current_salary * 1.07
    return new_salary

Pete_salary = 19000
Bob_salary = 40000

print "New Pete salary - ", pay_raise(Pete_salary)
print "New Bob salary - ", pay_raise(Bob_salary)
