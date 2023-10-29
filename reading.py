
# set a variable and link it  to the file ( make sure  the path  works)
# r+ - Read  and write, R - read, w - write or create a new file with the .write  text in  it.
emps = open("index.html", "w")
emps.write(" \n </html>Welcome To HTMl Life</a>")
# for employees in  emps.readlines():
#     print(employees)
##print(emps.read())
# print(emps.readline())
emps.close()
