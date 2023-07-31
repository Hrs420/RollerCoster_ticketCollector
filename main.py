print("Welcome to the RollerCoster RIde")
height = int(input("Enter your Height (in cm:) "))
bill = 0

if height>120 :
  print("You can Ride the Rollercoster !")
  age = int(input("Enter your Age: "))
  if age < 12:
    bill = 5 
    print("Child ticket is $5 ")

  elif age <= 18:
    bill = 7
    print("Youth Ticket is  $7")

  else:
    bill = 12
    print("Adult ticket is $12")

  wants_photo = input("Do you want photo? Y or N:  ")
  if(wants_photo == "Y"):
    bill+=3

  print(f"Your bill is ${bill}")
  
    
else:
  print("Sorry! You have to growup to ride the rollercoster! ")



  
