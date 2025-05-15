names_file = open("names.txt", "a")

name = input("What is your name? ")

names_file.write(name + "\n")

print("Name saved!")

names_file.close()