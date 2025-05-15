# if in the same directory just write the filename
# r stands for read
# w stands for write. it overwrites everthing in a file
# a stands for append ..you can only add to the file but cannot change anything in the file
# r+ stands for read and write
# open function would just open the file
# when you open a file always make sure to close it 
# readeable() allows use to check if a file is readable from and it returns a boolean
#read() reads the whole file
# readline() reads just a line
# readlines() puts each line in a list 

employee_file = open("employees.txt", "r")

for employee in employee_file.readlines():
    print(employee)


employee_file.close()