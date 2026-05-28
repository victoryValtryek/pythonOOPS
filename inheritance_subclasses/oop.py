class Employee:
    raise_amt = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + last + '@gmail.com'
        self.pay = pay
    
    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):
    raise_amt = 1.05

    def __init__(self, first, last, pay, prog_lang):
        # suitable for single inheritence as it is easy to maintain
        super().__init__(first, last, pay) # passes the first, last, pay to the employee class init method to let it handle the initialization this provides code reuse
        # Employee.__init__(self, first, last, pay) # alternative use in case of multiple inheritence
        self.prog_lang = prog_lang

class Manager(Employee):
    pass

# initially when we instantiate a Developer object it looks for constructor in the Developer Class if not found it looks up in the next Class immediate in the inheritance chain, this is called method resolution
# dev_1 = Developer('Vignesh Aravindh', 'B', 100000)
# dev_2 = Developer('ab', 'c', 120000)


# Gives details on the Class Methods and Attributes along with from where it is inherited
# print(help(Developer))

# print(dev_1.email)
# print(dev_2.email)

# dev_1 = Employee('Vignesh Aravindh', 'B', 100000)
# this doesnt change the Employee Class's raise_amt and it remains same as 4 %, which can be tested by running the above line and commenting the below one
# dev_1 = Developer('Vignesh Aravindh', 'B', 100000)
# dev_2 = Developer('ab', 'c', 120000)

# print(help(Developer)) this will print the raise_amt as a variable defined in the Developer Class

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)


dev_1 = Developer('Vignesh Aravindh', 'B', 100000, 'Python')
dev_2 = Developer('ab', 'c', 120000, 'Java')

print(dev_1.email)
print(dev_1.prog_lang)
print(help(Developer))