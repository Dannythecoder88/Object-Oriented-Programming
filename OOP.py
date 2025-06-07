
#Creates a class in which they have variables that correspond to name and pay but
#instead of manually typing everything out as seen with emp_1.first which would
#correspond to first name, the variable is the equivalent of this making the process
#much easier

#self is instance method and serves as a placeholder for 
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last= last
        self.pay= pay
        self.email = first + "." + last + "@company.com"

    def fullname(self):
        return '{} {}'.format(self.first,self.last)
        

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

#These are both different and seperate objects and are stored in different places
#in the memory because they correspond to different things
#print(emp_1)
# print(emp_2)

#emp_1.first = 'Corey'
# emp_1.last = 'Schafer'
# emp_1.email = 'Corey.Schafer@company.com'
# emp_1.pay = 50000
# emp_2.first= 'Test'
# emp_2.last = 'User'
# emp_2.email = 'Test.User@company.com'
# emp_2.pay = 60000

print(emp_1.email)
print(emp_2.email)

#need parenthesis because this is a method rather than attribute and without 
#parenthesis method is returned rather than return value of method
print(emp_2.fullname())

#{} set as placeholders for the first and last name so it can be applied to various objects
#print('{} {}'.format(emp_1.first,emp_1.last))

#both functions do the same thing but when ran on the class (Employee) it doesn't know 
#specifically which instance it is being applied to so it must be made evidant in 
#parenthesis
emp_1.fullname()
print(Employee.fullname(emp_1))
