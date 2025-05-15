number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]


for row in number_grid:
    for column in row:
      print(column)
      
    # Nigeria  jungle language
def translate( phrase ):
    translation = ""
    for letter in phrase:
        if letter in "Aa":
            translation = translation + "1"
        elif letter in "Ee":
            translation = translation + "2"
        elif letter in "Ii":
            translation = translation + "3"
        elif letter in "Oo":
            translation = translation + "4"
        elif letter in "Uu":
            translation = translation + "5"
        elif letter in " ":
            translation = translation + letter
        else:
            translation = translation + letter + "a"
    return translation

print(translate(input("Enter a phrase: ")))