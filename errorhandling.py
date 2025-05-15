
try:
    
    number = int(input("Enter a number: "))
    print(number)
    
except ZeroDivisionError as err:
    print(err)
except ValueError as err:
    print(err)

# handling errors with try/except block 

def reverse(text):
    i = len(text) - 1
    reversed_text = ""
    while i >= 0:
        reversed_text = reversed_text + text[i]
        i-=1
    return reversed_text 

print(reverse("stressed"))

