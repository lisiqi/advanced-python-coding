from abc import ABCMeta, abstractmethod

class IDepartment(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, employees):
        """Implement in subclasses"""
    
    @abstractmethod
    def print_department(self):
        """Implement in subclasses"""

class Sales(IDepartment):
    def __init__(self, employees):
        self.employees = employees
        
    def print_department(self):
        print(f"Sales Department: {self.employees}")

class Development(IDepartment):
    def __init__(self, employees):
        self.employees = employees
        
    def print_department(self):
        print(f"Development Department: {self.employees}")
        
class ParentDepartment(IDepartment):
    def __init__(self, employees):
        self.employees = employees
        self.base_employees = employees
        self.sub_departments = []
        
    def add(self, department):
        self.sub_departments.append(department)
        self.employees += department.employees
        
    def print_department(self):
        print("Parent Department")
        for department in self.sub_departments:
            department.print_department()
        print(f"Total Employees: {self.employees}")
        
dept1 = Sales(300)
dept2 = Development(500)

parent_dept = ParentDepartment(30)
parent_dept.add(dept1)
parent_dept.add(dept2)

parent_dept.print_department()