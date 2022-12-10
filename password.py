password = input("Password, please? \n>> ")

if len(password) <8:
    print("Passwords must be 8 caracters or more and use propper grammer. Try again.")
  
    password = input(" Password, please? \n>> ")
if len(password) <8:
    input("try again \n>> ")

else:
    print("welcome")
