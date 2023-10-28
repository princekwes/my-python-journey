fig1 = float(input(" Enter your first value: "))
action1 = input(" Enter Arithmetic action: + - * / ")
fig2 = float(input(" Enter your second Value: "))


if action1 == "+":
    return1 = fig1 + fig2
elif action1 == "-":
    return1 = fig1 - fig2
elif action1 == "*":
    return1 = fig1 * fig2
elif  action1 == "/":
    return1 = round(fig1 / fig2)
else:
    print(" Invalid  Operator   :) ")


print(" Your  Answer calculation is:", return1)
