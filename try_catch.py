try:
    value = 10/0
    number  = int(input(  "Enter a digit: "))
    print(number)
except ZeroDivisionError as  err1:
    print( " Divided by Zero")
    print(err1)
except ValueError as valerr:
    print(valerr)
    print( "Invalid  Error")