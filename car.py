
first = ""
while True:
   first = input("> ").lower()
   if first == "start":
      print( " Car Started... ")
   elif first == "stop":
      print( " Car Stopped... ")
   elif first == "help":
      print( """ 
Start - To Start  The Car
Stop  -  To Staop The Car
Quit - To  Stop The  Game """)
   elif first == "quit":
      break
   else: 
      print( " I  Dont Unnderstand ")
 