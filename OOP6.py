class Employee:

    def __init__(self, first, last):
        #These are attributes
        self.first = first
        self.last= last

#This allows the method (email) to be defined as a method but it can be accessed
#As an attribute so you dont need to call it with .email() as you would with
#Standard methods, but rather it can be called with just .email as an attribute would be
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)
    
#These def functions are methods
    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
#setter allows you to define how to change a property (turns method into fake attribute/variable)
#while making it look like you're assigning a attribute
    @fullname.setter
    def fullname(self, name):
        #makes first part before space in emp_1.fullname = 'Corey Schafer' to
        #the first name, and the last to after the space by using the split function
        first, last = name.split(' ')
        self.first = first
        self.last = last

#This deletes all data for a person such as their name, etc. and sets their name to
#None None so ex. when email is run such as at bottom, it's output is None.None@email.com
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None
    
emp_1 = Employee('John', 'Smith')

emp_1.fullname = 'Corey Schafer'

#This changes the first name attribute because it directly applies to it and also
#changes the full name because it is a method that is run everytime, however
#It doesn't change the email because it is in the main class and is only run one time
#therefore we must make a method that relates to the email so that it can run every time
#and be changeable. PS this is before email method was made
#emp_1.first = 'Jim'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname
print(emp_1.email)