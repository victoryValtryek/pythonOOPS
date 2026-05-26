class Employee:
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + self.last + '@gmail.com'
    
        Employee.num_of_emps += 1
    
    # Regular Methods
    def fullname(self):
        return f"{self.first} {self.last}"
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    # Class Methods
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amt = amount

    # Alternative Constructor
    @classmethod
    def fromstring(cls, emp_str):
        first, last, pay = emp_str.split(sep='-')
        return cls(first, last, pay)

    @staticmethod
    def isworkday(day):
        return True if day in [1, 2, 3, 4, 5] else False

emp_1 = Employee('Vignesh Aravindh', 'B', 90000)
emp_2 = Employee('DD', 'V', 80000)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

Employee.set_raise_amount(1.06)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

# updating by using the instance variable that calls class method has same effect as calling the class method with class name
# emp_1.set_raise_amount(1.07)
# print(Employee.raise_amt)
# print(emp_1.raise_amt)
# print(emp_2.raise_amt)

# alternative constructors
# used when we want to do some pre-processing to the input before creating or instantiating an object

# input
emp_str_1 = 'ab-c-100000'

# manual way
first, last, pay = emp_str_1.split(sep='-')
emp_3 = Employee(first, last, pay)
print(emp_3.email)

# the above one has redundancy has for every employee we need to write the code for splitting again
# we can use alternative constructor to solve the above problem
# use class methods as pre-processors before instantiating the object
emp_4 = Employee.fromstring("xy-z-899999")
print(emp_4.email)

# static methods - included in class as they have a logical connection with the class, but don't take class or instance as an argument
# static methods are those methods that do not access the instance or class name directly
print(Employee.isworkday(5))