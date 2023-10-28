secret_word = "giraffe"
guess = ""
count = 0
while guess != secret_word:
    guess = input( " Enter a secred word: \n")
    
    if guess ==  secret_word:
        print( " Got You! You Got it.")
   
