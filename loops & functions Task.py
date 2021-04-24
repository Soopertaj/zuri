

import random
data_base = {9447270565:["Soliah","taj","stajliad@gmail.com", "password", 1000]}

def init():
    print("****** Welcome to Solz Bank!****** \n")
    Custormer = int(input("Do you have an account with us? (1.) Yes, login (2.) No, register. \n "))\

    if Custormer==1:
        login()

    elif Custormer==2:
        Register()
    
    else:
        print("You have seected an ivalid option!")
        init()


def Register():
    print("****** Registeration *******")
    first_name = input("Pease enter your First name \n")
    last_name = input("please enter your last name \n")
    Email = input("Please Enter your Email address \n")
    password = input("Please enter your password \n")

    account_number = Generating_account()

    data_base [account_number] = [first_name, last_name, Email, password]

    print("Your account has been successfully created! \n")
    print("Your account number is: %d \n" % account_number)
    print("Please login \n")

    login()

def Generating_account():
    return random.randrange(1111111111,9999999999)

def login():
    print("####### Login ##############")
    Custormer_account = int(input("What is your account number? \n"))
    Custormer_password = input("What is your password? \n")

    for account_number, User_details in data_base.items():
        if account_number==Custormer_account:
            if User_details[3]==Custormer_password:
                bank_operation(User_details)
        else:
            print("Inalid Account number or password!")
            login()

 
def bank_operation(user):
    print("Welcome to Solz bank %s %s" %(user[0], user[1]))
    print("What would you like to do? \n") 
    operation =int(input("(1.) Deposit (2.)Withdrawl (3.) Check Balances (4.)Home (5.)Exit \n"))

    if operation==1:
        deposit() 

    elif operation==2:
        withdrawl() 

    elif operation==3:
        Check_balances()

    elif operation==4:
        init()

    elif operation==5:
        exit()

    else:
        print("You have selected an invalid option! \n")
        bank_operation(user)

def deposit():

    current_balance = Account_balance()
    deposit = int(input("How much do you want to Deposit? \n"))
    current_balance = current_balance + deposit
    print("Your current balance is:#",current_balance)
    


def withdrawl():
    current_balance = Account_balance()
    withdraw = int(input("How much do you want to withdraw? \n"))
    if current_balance >= withdraw:
        current_balance = current_balance - withdraw
        print("You have succesfully withdrew %d! \n" %withdraw) 
        print("Your account balance is:#",current_balance)
        

    else:
        print("You have insufficient balance!")
        withdrawl()
    

def Check_balances():
    print("Your Account Balance is:#",Account_balance())
    

def Account_balance():
    for key,value in data_base.items():
        return value[4]



init()



    