def my_name(name):
    print("my name is " +name)
my_name("zahraa")
def my_meal(food , drink):
    print("i like to eat " +food+ " while drinking " +drink)
my_meal("pizza" , "cocktail juice")
def cube(number):
    return number*number*number
def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False
result = by_three(5)
print(result)