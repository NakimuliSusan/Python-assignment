def sum_and_greet (*args , **kwargs):
    sum = 0
    for num in args:
        sum+=num
    keys = kwargs.keys()
    if "name" in keys :
        print(f"Hello {kwargs['name']} the answer is {sum}")
    elif "country" & "name"  in keys :
        print(f"Hello  {kwargs['country']}, the answer is {sum}.")
    elif not kwargs:
        print(f"Hello Annonymus the answer is {sum}.")
# sum_and_greet(1,2,3,4, name = "Susan")
# sum_and_greet(10,20,30,40, name="Effence", country = "Kenya")
# sum_and_greet(name = "Verite")
# sum_and_greet(100,1000,10000)