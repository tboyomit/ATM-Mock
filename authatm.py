# Register
# -First name, Last name, email, username, password
# -generate user id

# Login
# -account number (username or email), and password

# System Initializing
import random
import datetime as dt

database = {
    4515303556: ["Tobiloba", "Omitola", 'tboyomit@gmail.com', 'good', 350745],
    4237367278: ["Seyi", "Onifade", 'seyi@zuri.team', 'passeyi', 15000],
    2748590466: ["Sumat", "Rajan", 'sumrat@zuri.team', 'sumpas', 800]
}                                                                                       # dictionary for database


def init():
    current_datetime = dt.datetime.now()
    print(current_datetime)
    print('=============================================')
    print('           Welcome to Utopia Bank')
    print('=============================================')

    valid_status_option = False
    while not valid_status_option:

        account_status = int(input('Do you have an account with us? Select 1 (Yes) or 2 (No) \n'))

        if account_status == 1:
            login()
        elif account_status == 2:
            register()
        else:
            print('**You have selected an invalid option**')


def register():

    print("====================================")
    print('******Register for an account******')
    print("====================================")

    email = input('Enter your email address \n')
    first_name = input('Enter your First name \n')
    last_name = input('Enter your Last name \n')
    password = input('Enter your password \n')

    account_number = generate_account_number()
    database[account_number] = [first_name, last_name, email, password, 0]

    print("=======================================")
    print('Your account has been created')
    print("=======================================")
    print("Your account number is: %d" % account_number)
    print("Please keep it safe")
    print("=======================================")

    login()


def login():

    print("====================================")
    print('***************Log in***************')
    print("====================================")

    login_successful = False
    while not login_successful:

        AccNumUserInp = int(input('Enter your account number \n'))
        PassUserInp = input('Enter your password \n')

        for account_number, user_info in database.items():
            if AccNumUserInp == account_number:
                if PassUserInp == user_info[3]:
                    bank_operation(user_info)

        print('**Invalid account number or password**')  # Serves as response to the while loop for when login fails


def bank_operation(user_info):

    print('===================================')
    print('**Log in successful**')
    print('      Welcome %s %s          ' % (user_info[0], user_info[1]))
    print('===================================')
    print('Deposit: Select (1)')
    print('Withdrawal: Select (2)')
    print('Balance: Select (3)')
    print('Complaints: Select (4)')
    print('Log out: Select (5)')
    print('Exit: Select (6)')

    valid_select_option = False
    while not valid_select_option:
        selectOption = int(input('Please select an option: \n'))

        if selectOption == 1:
            deposit_operation(user_info)

        elif selectOption == 2:
            withdrawal_operation(user_info)

        elif selectOption == 3:
            get_balance_operation(user_info)

        elif selectOption == 4:
            complaint()

        elif selectOption == 5:
            logout()

        elif selectOption == 6:
            exit()

        else:
            print('**Invalid option selected**')


def deposit_operation(user_info):

    valid_deposit = False
    while not valid_deposit:
        deposit = int(input("How much do you want to deposit? \n"))

        if deposit > 50000:
            print("Amount exceeds deposit limit of #50,000 \nPlease try again")

        else:
            totalBalance = deposit + user_info[4]
            print(f"You deposited #{deposit}")
            print(f"Your current balance is now #{totalBalance}")

        triage()


def withdrawal_operation(user_info):

    print("How much do you want to withdraw?")
    print("(1) 1000 (2) 2000 (3) 5000")
    print("(4) 10000 (5) Others")

    valid_withdraw_amount_opt = False
    while not valid_withdraw_amount_opt:

        withdraw_amount_opt = int(input())

        if withdraw_amount_opt == 1:

            if user_info[4] >= 1000:
                print("Please take your cash")
                print(f"You current balance is #{(user_info[4]-1000)}")
            else:
                print("Insufficient balance")

        elif withdraw_amount_opt == 2:

            if user_info[4] >= 2000:
                print("Please take your cash")
                print(f"You current balance is #{(user_info[4] - 2000)}")
            else:
                print("Insufficient balance")

        elif withdraw_amount_opt == 3:

            if user_info[4] >= 3000:
                print("Please take your cash")
                print(f"You current balance is #{(user_info[4] - 3000)}")
            else:
                print("Insufficient balance")

        elif withdraw_amount_opt == 4:

            if user_info[4] >= 5000:
                print("Please take your cash")
                print(f"You current balance is #{(user_info[4] - 5000)}")
            else:
                print("Insufficient balance")

        elif withdraw_amount_opt == 5:

            valid_withdraw_amount = False
            while not valid_withdraw_amount:

                withdraw_amount = int(input("How much do you want to withdraw? \n"))

                if withdraw_amount > 20000:
                    print("Amount exceeds withdrawal limit of #20000\nPlease try again")

                else:

                    if user_info[4] >= withdraw_amount:
                        print("Please take your cash")
                        print(f"You current balance is #{(user_info[4] - withdraw_amount)}")
                    else:
                        print("Insufficient balance")

                triage()
        else:
            print("**Invalid option selected** \nPlease try again")

        triage()


def get_balance_operation(user_info):
    print("Your balance is #%d " % user_info[4])

    triage()


def complaint():
    print("======================================================")
    print("You can reach the customer care through the following:")
    print("Tel: 972987938472, 09823984792")
    print("Email: customercare@utopiabank.com")
    print("Web: www.utopiabank.com")
    print("======================================================")
    print("Thank you for banking with us")
    print("======================================================")

    triage()


def logout():
    print("**You have now logged out**")
    init()


def triage():

    print('Do you want to perform another transaction?')
    valid_decision = False
    while not valid_decision:
        decision = int(input('Select: (1) Yes (2) No \n'))

        if decision == 1:
            login()
        elif decision == 2:
            logout()
        else:
            print('**Invalid option selected**')


def generate_account_number():
    return random.randrange(1111111111, 9999999999)


init()
# withdrawal_operation()
