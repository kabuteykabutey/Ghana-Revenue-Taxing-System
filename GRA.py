def ussd_menu():
    print("Welcome to TaxLink Ghana")
    print("1. Register")
    print("2. Make payment")
    print("3. View Tax Status")
    choice = input("Select an option: ")

    if  choice == "1":
        register()
    elif choice == "2":
        make_payment()
    elif choice == "3":
        view_stat()
    else:
        print("Invalid option. Please try again.")
        return choice

def register():
    reg_num = input("Enter your Ghana Card Number: ")
    print("1. Trader\n2. Mason\n3. Hairdresser\n4. Carpenter\n5. Plumber")
    trade  =  input("selct your trade: ")

    print(f"Registration successful!\nYour Tax ID: TXGHA-{reg_num[-4:]}")

def make_payment():
    print('Enter payment Method:\n1. Bank transfer\n 2.MoMo User ')
    choice1 = input("Enter your choice: ")
    if choice1 == "1":
        amount = float(input("Enter amount to pay (GHS): "))
        tax = amount - (amount * (25 / 100))
        number = int(input('Enter banking number: '))
        if number <= 9999999999999:
            print('=============================================')
            print(f"Tax after 25% deduction: GHS {tax}")
            print(f"Payment of GHS {amount} to account number: {number} .\n tax deducted from your acount is GHC")
        else:
            print('Incorrect bank number')
    elif choice1 == "2":
        amount = float(input("Enter amount to pay (GHS): "))
        tax = amount - (amount * (25 / 100))
        number = int(input('Enter recipient number: '))
        if number <= 999999999:
            print(f"Tax after 25% deduction: GHS {tax}")
            print(f"Payment of GHS {amount} to {number} .\n tax deducted from your acount is GHC")
    else:
        print("Invalid option. Please start over.")

def view_stat():
    print('Status: Active')

def start_ussd():
    short_code = input('Please input the short code: ')
    if short_code == '*800#':
        ussd_menu()
    else:
        print("Invalid option. Please try again.")
        return short_code

start_ussd()
