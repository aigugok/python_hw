class Employee:
    def __init__(self,name,age,profession,is_working=True):
        self.name=name
        self.age=age
        self.profession=profession
        self.is_working=is_working
    def employee_is_working(self):
        if (self.is_working):
            return f"{self.name} is working in the company as an {self.profession}"
        return f"{self.name} is a former employee, was an {self.profession}"

Mary=Employee("Mary",34,"accountant")
print(Mary.employee_is_working())

import pickle
with open('hw14_1.py', 'wb') as f:
    pickle.dump(Mary, f)
del(Mary)

with open('hw14_1.py', 'rb') as f:
    data_new = pickle.load(f)
print(data_new.age)