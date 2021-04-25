# Register
# -First name, Last name, email, username, password
# -generate user id

# Login
# -account number (username or email), and password

# System Initializing
import random
import datetime as dt

database = {
    4515303556: ["Tobiloba", "Omitola", 'tboyomit@gmail.com', 'hoodrush', 350745],
    4237367278: ["Seyi", "Onifade", 'seyi@zuri.team', 'passeyi', 164500],
    2748590466: ["Sumat", "Rajan", 'sumrat@zuri.team', 'sumpas', 72500]
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
    print('Transfer: Select (4)')
    print('Complaints: Select (5)')
    print('Log out: Select (6)')
    print('Exit: Select (7)')

    valid_select_option = False
    while not valid_select_option:
        selectOption = int(input('Please select an option: \n'))

        if selectOption == 1:
            deposit_operation()

        elif selectOption == 2:
            withdrawal_operation()

        elif selectOption == 3:
            get_balance_operation(user_info)

        elif selectOption == 4:
            transfer_operation()

        elif selectOption == 5:
            complaint()

        elif selectOption == 6:
            logout()

        elif selectOption == 7:
            exit()

        else:
            print('**Invalid option selected**')


def deposit_operation():
    print("Deposit Operations")

    triage()


def withdrawal_operation():
    print("Withdrawal Operations")

    triage()


def set_current_balance(user_info, balance):
    balance = user_info[4]

def get_balance_operation(user_info):
    print("Your balance is #%d " % user_info[4])
    # userBal = balance[allowedUser.index(name)]
    # return user_info[4]

    triage()


def transfer_operation():
    print("Transfer Operations")

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


def triage():

    print('Would you like to perform another transaction?')
    valid_decision = False
    while not valid_decision:
        decision = int(input('Select: (1) Yes (2) No \n'))

        if decision == 1:
            login()
        elif decision == 2:
            logout()
        else:
            print('**Invalid option selected**')


def logout():
    print("**You have now logged out**")
    init()


def generate_account_number():
    return random.randrange(1111111111, 9999999999)


init()
