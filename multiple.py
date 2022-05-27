
def greet_multiple (*names):
    for name in names:
        print(f"Hello {name}")
    
def get_year (*ages , **kwargs):
    for age in ages:
        year  = 2022 - age
        next_year = 2022 + 1
        print(f" Hello {kwargs['name']}, You were born in {year}. Your age is {age} years old an your from {kwargs['country']} and your next_year's birthday is {next_year}")

get_year(23,22,21,20,19,18, country = "Uganda" , name = "Aicets")
get_year(108, country = "Uganda" , name = "Busingye")
get_year(22, country = "Uganda" , name = "Aicets")

