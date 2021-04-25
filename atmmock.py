AllowedUsers =  ['Seyi','Mike','Love']
AllowedPassword = ['passwordSeyi','passwordMike','passwordLove']

print('Welcome to Python bank')
name = input('What is your name? \n')

if(name in AllowedUsers):
    password = input('What is your password? \n')
    userId = AllowedUsers.index(name)

    if(password == AllowedPassword[userId]):

            import datetime as dt
            current_datetime = dt.datetime.now()
            print(current_datetime)

            print('Welcome %s' %name)
            print('These are the available options:')
            print('1. Withdrawal')
            print('2. Deposit')
            print('3. Complaint')

            SelectedOption = int(input('Please select an option: \n'))

            if(SelectedOption == 1):
                withdrawal_amount = int(input('How much would you like to withdraw? \n'))
                print('Please take your cash')
                print('Thank you for banking with us')

            elif(SelectedOption == 2):
                deposit_amount = int(input('How much would you like to deposit? \n'))
                print('Your current balance is #%d' %deposit_amount)

            elif(SelectedOption == 3):
               complaint_type = input('What issue will you like to report? \n')
               print('Thank you for contacting us. Your complaints has been received')
               
            else:
                print('Invalid Option selected, please try again')
                
    else:
            print('Password Incorrect, please try again')
else:
    print('Name not found, please try again')

                 
