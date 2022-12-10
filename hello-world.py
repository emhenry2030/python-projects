import time

def promptForPassword():
  password = input("password, please. \n>> ")
  isValid = validatePassword(password)
  if(isValid):
    promptForBirthYear()
  else:
    promptForPassword()
    

def validatePassword(password):
  isValid = False
  if len(password) < 8:
    handleInvalidPassword()
  else:
    isValid = True
  return isValid  
    
    
def handleInvalidPassword():
    print("Password must be 8 letters/numbers or more. try again.")
    
    
def promptForBirthYear():
  print ("Welcome. This program will show you how old you will be in 2030. Now i will have to ask you a question. Pease anser it below.")

  birthYear = input("what year were you born? \n>> ")

  birthYearAsInteger = int(birthYear)


  yourAgeIn2030 = (2030 -birthYearAsInteger)

  time.sleep(2)

  print ("Wait, wait, almost done")

  time.sleep(2)

  print(yourAgeIn2030)

  playAgain = input("play again? press y if yes or n for no \n>> ")
 
  if playAgain == "y":
    promptForPassword()
  else:
    print("Have a great day!")

promptForPassword()

