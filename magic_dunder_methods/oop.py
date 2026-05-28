class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = last + '@gmail.com'
    
    def fullname(self):
        return f"{self.first} {self.last}"
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    # special methods are used to change the behaviour of normal functionality defined generally using double underscores
    # double underscores are called dunder

    # unambigous representation of object and should be used for logging and debugging - for developers
    def __repr__(self):
        return f"Employee {self.first, self.last, self.pay}"

    # readable representation of the object used for end users
    def __str__(self):
        return f"{self.fullname()} - {self.email}"
    
    def __add__(self, other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())
        # return NotImplemented

emp_1 = Employee('Vignesh Aravindh', 'B', 90000)
emp_2 = Employee('ab', 'c', 80000)

# print(1 + 2)
# print('a' + 'b')

# print(emp_1)
# print(repr(emp_1))
# print(str(emp_1))

# print(emp_1.__repr__())
# print(emp_1.__str__())

print(int.__add__(1, 2))
print(str.__add__('a', 'b'))

# operator overloading
print(emp_1 + emp_2)

print(Employee.__add__(emp_1, emp_2))

print(len("test"))
print(str.__len__("test"))

print(len(emp_1))
print(Employee.__len__(emp_1))