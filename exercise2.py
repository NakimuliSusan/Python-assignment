from unicodedata import name

def sum (*numbers):
    x = 0
    for number in numbers:
        x+=number
    return(x)

def multiply(*numbers):
    y = 1
    for number in numbers:
        y*=number
    return (y)

def greet_multiple (**kwargs ):
    print(kwargs.keys())
    print(kwargs.values())
    keys = kwargs.keys()
    if "country" in keys :
        print(f"Hello {kwargs['name']} your are from {kwargs['country']} ")
    elif "age" in keys:
        year = 2022 - kwargs['age']
        print(f"Hello {kwargs['name']} you were born in {year}")
    elif not kwargs:
        print(f"Hello Annyonomus")

greet_multiple(name = "Susan" , country = "Uganda")
greet_multiple(name = "Susan" , age= 22 , school = "AkiraChix")
greet_multiple()



   