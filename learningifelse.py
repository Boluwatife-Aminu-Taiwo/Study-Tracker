is_male = False
is_tall = True

if is_male and is_tall : 
    print("He is an Alpha Male")
elif is_male and not(is_tall):
    print("He is a Beta Male")
elif not(is_male) and is_tall:
    print("She is an Alpha Female")
else:
    print("She is a Beta Female")

# if i make an if statement it is gonna work as long as the condition is true
# not is used to say if false

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
    
print(max_num(299,32,8))

num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

def calculator(num1, op, num2):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        return num1 / num2
    else :
        return "Please input a valid number or operator"
    
print(calculator(num1, op, num2))