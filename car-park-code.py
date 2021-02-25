from pandas import DataFrame

carPark = []
for row in range (0,10):
  carPark.append([])
  for column in range(0,6):
    carPark[row].append("Empty")

def menuSystem():
  menu = True
  while menu == True:
    print("------------------------------------------")
    print("Welcome to the Taylor car park menu system")
    print("------------------------------------------")
    print("1 - Set all spaces to empty")
    print("2 - Park a car")
    print("3 - Remove a car")
    print("4 - Display car park")
    print("0 - Exit menu system")
    option = int(input("Please enter the option number: "))
    if option == 1:
      emptyCarPark(carPark)
    elif option == 2:
      parkCar(carPark)
    elif option == 3:
      removeCar(carPark)
    elif option == 4:
      displayCarPark(carPark)
    elif option == 0:
      print("Thank you for visiting")
      menu = False
    else:
      print("Invalid entry")

def emptyCarPark(carPark):
  for row in range(0,10):
    for column in range(0,6):
      carPark[row][column]="Empty"
  print("The car park has been cleared")
  print(DataFrame(carPark))

def parkCar(carPark):
  regNo = input("Please enter your car's registration: ")
  print("Please enter the space you would like to park in")
  rowNo = int(input("Row number: "))
  columnNo = int(input("Column number: "))
  if carPark[rowNo-1][columnNo-1] == "Empty":
    carPark[rowNo-1][columnNo-1] = regNo
    print("This space is avaliable")
    print("Parking complete")
  else:
    print("This space is currently unavaliable")
    print("Please try somewhere else")

def removeCar(carPark):
  regNo = input("Please enter your car's registration: ")
  print("Please enter the space you parked in: ")
  rowNo = int(input("Row number: "))
  columnNo = int(input("Column number: "))
  if carPark[rowNo-1][columnNo-1] == regNo:
    carPark[rowNo-1][columnNo-1] = "Empty"
    print("Your car has been located")
    print("Car removed")
  else:
    print("Your car has not been located in this space")

def displayCarPark(carPark):
  print(DataFrame(carPark))



menuSystem()
