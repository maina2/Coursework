actual_word = "password"
guess = ""
max_attempts = 3
attempts = 0
out_of_guesses = False



while  guess != actual_word and not(out_of_guesses) :
    
    if max_attempts > attempts :
        guess = str(input("Guess the word :"))
        
        attempts+=1

    else:
       
        out_of_guesses = True

    
if out_of_guesses:
    print("You failed to get the correct word")

else:
    print("you got the right word")
    
# while not(guess) == actual_word 