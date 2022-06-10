class Student:
    school = "AkiraChix" 
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    
    def full_name(self):
        return f"Hello {self.first_name}{self.last_name}"

    def year_of_birth(self):
        year = 2022 -self.age
        return f"Hello {self.full_name} your were born in {year} and your age is {self.age}"

    def get_intials(self):
        intial = self.first_name[0] + self.last_name[0]
        return intial.upper()

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