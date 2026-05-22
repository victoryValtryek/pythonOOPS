class Employee:
    # The 'self' is just a standard name can be anything
    def __init__(self, name, email):
        # Attributes of the Class
        self.name = name
        self.email = email
    
    def details(self):
        return '{} has mail id {}.'.format(self.name, self.email)

emp_1 = Employee('Vignesh Aravindh B', 'vignesharavindh@amat.com') # instance of Employee Class with Automatic Creation of Instance Variable
emp_2 = Employee('DD', 'dd@ibm.com') # instance of Employee Class automatically runs the init method

print(emp_1)
print(emp_2)

# Instance Variable - Method 1 Manual Creation - Time consuming and repetitive
# emp_1.name = "Vignesh Aravindh B"
# emp_1.email = "vignesharavindh@amat.com"

# emp_2.name = "DD"
# emp_2.email = "dd@ibm.com"

print(emp_1.name)
print(emp_2.name)

# Function but again repetetive to use when there are many instance variable hence we need Class Methods
print('{} has mail id {}.'.format(emp_1.name, emp_1.email))

# Class Method we can use for any instance variable
# Provides Code Re-Use 
print(emp_1.details())
print(emp_2.details())

# Use Class Name Directly
print(Employee.details(emp_1)) 
print(emp_1.details()) # when we run this the above statement is what that goes in the background