# it loops until a conditon is met or false
# while loops loop until condition is false
# format while condition: then code below, code moves as long as condtion is true

# i = 1

# while i <= 10: 
#     print(i)
#     i += 1
    
# print("Done with loop")

# secret_word = "Bolu"
# guess = ""
# guess_count = 0
# guess_limit = 3
# is_outofGuess = False

# while guess != secret_word and not(is_outofGuess):
#     if guess_count < guess_limit:
#         guess = input("Enter guess: ")
#         guess_count += 1
#     else:
#         is_outofGuess = True

    
# if guess == secret_word:
#     print("You win!")
# else:
#     print("You are out of guesses")
    

# i = 5 

# while i != 0:
#     print(i)
#     i -= 1
    
# break stops the loop at that iteration 
# continue skips that iteration and continues


def raise_to_power(base_num, pow_num):
    return base_num**pow_num

print(raise_to_power(3,4))