# def greeting( name, age ):
#     print("Greetings " + name)
#     print("You are " + age + " years old I presume")

# name = input("Enter name: ")
# age =  str(input("Enter age: "))
# greeting(name, age)

# return is to get information from a function
#writing anything after return in a function doesnt work because python breaks out after return

def cube_num( num ):
    return num * num * num

print(cube_num(3))