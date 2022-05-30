class Student:
    school = "AkiraChix" 
    def __init__(self,name,year_of_birth):
        self.name = name
        self.year_of_birth = year_of_birth
    
    
    def full_name(self):
        return f"Hello {self.name}, your welcome to {self.school}"

    def greeting(self):
        age = 2022 - self.year_of_birth 
        return f"Hello {self.name} your were born in {self.year_of_birth} and your age is {age}"

    def get_intials(self):
        intials = ""
        full_name = self.name.split()
        for name in full_name: 
           intials += name[0]. upper() 
        return intials

    #class Student
    # def full_Name(self):
    #     first_Name = int(input("Enter first name:"))
    #     second_Name = int(input("Enter second name:"))
    #     full_Name = first_Name + " " + second_Name
    #     return full_Name
    # school = 'AkiraChix'

    # def __init__(self,name,age,country):
    #     self.name = name
    #     self.age = age
    #     self.country = country

    # def greeting (self):
    #     return f"Hello {self.name} from {self.country}, welcome to {self.school}"