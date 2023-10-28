price = 1000000
credit_high = 80
credit_low = 79

credit = input(" Please State Your Credit level: ")

if int(credit) >=  80:
    down_pay = price * 0.10
    print(" based on  your credit level [  which is above 80% ], you will Pay: " + str(down_pay) + "$ as down payment" )
elif int(credit) <= 79:
    down_pay = price * 0.20
    print(" based on  your credit level [  which is less than 80% ], you will Pay: " + str(down_pay) + "$ as down payment" )

print("Thank You and Welcome")
