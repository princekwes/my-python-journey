# name = input("Please Enter Your Full Name: ")

# text  = name.split()


# for i in text:
#     print(i)
# print(text[0].lower())
# print(text)



text = "arn:aws:iam::123456789012:user/johndoe"
name = text.split("/")
name2 = name[1]
name3 = text[:text.index("user")]

print(text)
print("*****************************")
print(name)
print("*****************************")
print(name2)
print("*****************************")
print(name3)
