allowedUser = ['Rowland' , 'Balogun' , 'Courage' , 'David']
balance = [678900 , 4910000.87 , 5428690 , 376800]
allowedPassword = ["rowlandPass" , "balogunPass" , "couragePass" , "davidPass"]

name = input("Enter you name: \n")

if name in allowedUser:
    password = input("Enter your password: \n")
    userId = allowedUser.index(name)

    if password == allowedPassword[userId]:
        print("")
        print("First Bank Nigeria")
        print("Welcome " + name )
        print("")

        print("Press 1 to Check Balance")
        print("Press 2 to Make Deposit")
        print("Press 3 to Withdraw")
        print("Press 4 to check our Customer Care Info")
        print("")

        selectedOption = int(input("Enter your desired option: "))
        userBal = balance[allowedUser.index(name)]

        if selectedOption == 1:
            print(f"Your balance is #{userBal}")

        elif selectedOption == 2:
            print("How much do you want to Deposit?")
            deposit = int(input())
            if deposit > 100000:
                print("The maximum deposit you can do is #100,000 \n Please try again")
            else:
                totalBalance = deposit + userBal
                print(f"Your total balance is now #{totalBalance}")

        elif selectedOption == 3:
           print("How much do you want to withdraw?")
           withdraw = int(input())
           remainBalance = userBal - withdraw
           if withdraw > 50000:
               print("The maximum withdrawal is #50,000 \n Please try again")
           else:
               print("Please take your cash")
               print(f"You remaining balance is now #{remainBalance}")

        elif selectedOption == 4:
            print("You can reach the customer care through the following:")
            print("Tel: 972987938472, 09823984792")
            print("Email: customercare@firstbank.com")
            print("Web: www.firstbank.com")
            print("")
            print("Thanks for banking with us")

    else:
        print("Password incorrect, please try again")
else:
    print("You are not allowed to login")