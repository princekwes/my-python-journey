secret_word = "giraffe"
guess = ""
count = 0
count_limit = 3
out_of_guesses = False
while guess != secret_word and not(out_of_guesses):
    if count < count_limit:
         guess = input( " Enter a secred word: \n")
         count += 1
    else:
        out_of_guesses = True
if  out_of_guesses:
        print( " Out  Of  Guesses, You Lose!")
else:
        print( " Got You! You Got it.")
   
