num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the Second number: "))

while True:
    print("\nPress 1 for Addition \nPress 2 for Subtraction \nPress 3 for Multiplication \nPress 4 for Division\npress 5 for Exit")

    choice = int(input("Enter your choice from 1-5 : "))

    if choice == 1:
        print("Addition of the numbers is:", num1+num2)
    elif choice == 2:
        print("Subtraction of the numbers is:", num1-num2)
    elif choice == 3:
        print("Multiplication of the numbers is:", num1*num2)
    elif choice == 4:
        print("Division of the numbers is:", num1/num2)
    elif choice == 5:
        print("Exiting application. Goodbye!")
        break
    else:
        print("input invalid")
