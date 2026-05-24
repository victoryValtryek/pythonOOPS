class Employee:
    location = 'Chennai'
    def __init__(self, name, email):
        self.name = name
        self.mail = email
        # self.location = ''

    def email(self):
        return f"{self.name} has email {self.mail}."
    
    def set_location(self):
        self.location = Employee.location # need a class name or instance name direct access to calss variable will throw Name Error

    def get_location(self):
        return self.location

emp_1 = Employee("Vignesh Aravindh", "vignesharavindh@amat.com")
emp_2 = Employee("DD", "dd@ibm.com")

# its better to get the location commonly for all instances or possibly using Employee.location, need direct access to access and modify it
# print(emp_1.get_location())
# emp_1.set_location()
# print(emp_1.get_location())


'''All these cases are due to the instance variable created during constructor creation'''
# Case - 1
'''Here when we change the location of emp_1 to Bangalore then the value of the instance's variable changes when doing set_location() again the original class varible that has Chennai gets assigned back. So there is Scoping for instance and class variable'''
# emp_1.location = 'Bangalore'
# emp_1.set_location()
# print(emp_1.get_location())
# emp_2.set_location()
# print(emp_2.get_location())


# Case - 2
'''Here the emp_1 location gets printed as Bangalore and emp_2 which has the Class Variable Value prints Chennai'''
# emp_1.location = 'Bangalore'
# print(emp_1.get_location())
# emp_2.set_location()
# print(emp_2.get_location())


# Case - 3
'''Here when we change the class variable to Bangalore still the instance variable of emp_1 that were assigned previously as Chennai remains as is due to scoping and local instance copy of location variable where as the emp_2 prints Bangalore because we update it again'''
# Employee.location = 'Bangalore'
# print(emp_1.get_location())
# emp_2.set_location()
# print(emp_2.get_location())


# Case - 4
'''Here both emp_1 and emp_2 gets updated to new Class Variable as we set them manually again using Class Method set_location()'''
# Employee.location = 'Bangalore'
# emp_1.set_location()
# print(emp_1.get_location())
# emp_2.set_location()
# print(emp_2.get_location())

'''This means whenever we update Class Variable in Class Scope it is not updated automatically for the copy of it in the instance Scope. Class Scope vs Instance Scope'''

print(Employee.__dict__) # 
print(emp_1.__dict__) # doesnot have the Class Variable

print(emp_1.location)
Employee.location = 'India' # changing this changes the instances value as well
print(emp_1.location) # doesnt have the location variable in its instance memory or dict
print(emp_1.__dict__)

emp_1.location = 'Chennai' # creates a location variable in its instance memory as a copy or dict
print(emp_1.location)
print(emp_1.__dict__)
print(emp_2.location)
print(emp_2.__dict__)

Employee.location = 'Bangalore'
print(emp_1.location) # retains Chennai as right now this instance has its own copy of the Class Variable
print(emp_1.__dict__)
print(emp_2.location)
print(emp_2.__dict__)