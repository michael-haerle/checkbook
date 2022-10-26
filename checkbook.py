import os
import sys

# DO NOT RUN IN VS CODE

print('--- Welcome to your terminal checkbook ---\n')
print('What would you like to do?\n')
print('1) View current balance')
print('2) Record a debit (withdraw)')
print('3) Record a credit (deposit)')
print('4) Exit')

def checkbook_app():
    x = input('Your choice?')
    if x != '1' and x != '2' and x != '3' and x != '4':
        print('Choice not vaild please select the number from the list given.')

    else:
        while x == '1':
            print('test')
            with open('checkbook_balance.txt', 'r') as balance:
                active_balance = balance.read()
                print(active_balance)
                active_balance = float(active_balance)
                active_balance = '{:.2f}'.format(active_balance)
            print('\nYour current balance is $', active_balance)

            continue_trans = ''

            while continue_trans != 'No' and continue_trans != 'Yes':
                print('\n')
                continue_trans = input('Would you like to make another transaction? Yes/No')

                if continue_trans == 'No':
                    sys.exit('\nThanks, have a great day!')
                elif continue_trans == 'Yes':
                    checkbook_app()
                else:
                    print('Not a vaild choice. Please type Yes or No.')


        while x == '2':
            with open('checkbook_balance.txt', 'r') as balance:
                active_balance = balance.read()
                active_balance = float(active_balance)
                active_balance = '{:.2f}'.format(active_balance)
                print('\nYour current balance is $', active_balance)

            app = 'active'
            while app == 'active':
                debit = input('How much is the debit?')
                debit = float(debit)
                new_balance = float(active_balance) - debit
                new_balance = float(new_balance)
                new_balance = '{:.2f}'.format(new_balance)
                app = ''

            with open('checkbook_balance.txt', 'w+') as balance:
                balance.write(new_balance)
            print('\nYour current balance is $', new_balance)

            continue_trans = ''

            while continue_trans != 'No' and continue_trans != 'Yes':
                print('\n')
                continue_trans = input('Would you like to make another transaction? Yes/No')

                if continue_trans == 'No':
                    sys.exit('\nThanks, have a great day!')
                elif continue_trans == 'Yes':
                    checkbook_app()
                else:
                    print('Not a vaild choice. Please type Yes or No.')

        while x == '3':
            with open('checkbook_balance.txt', 'r') as balance:
                active_balance = balance.read()
                active_balance = float(active_balance)
                active_balance = '{:.2f}'.format(active_balance)
                print('\nYour current balance is $', active_balance)

                app = 'active'
            while app == 'active':
                credit = input('How much is the credit?')
                credit = float(credit)
                new_balance = float(active_balance) + credit
                new_balance = float(new_balance)
                new_balance = '{:.2f}'.format(new_balance)
                app = ''
            
            with open('checkbook_balance.txt', 'w+') as balance:
                balance.write(new_balance)
            print('\nYour current balance is $', new_balance)

            continue_trans = ''

            while continue_trans != 'No' and continue_trans != 'Yes':
                print('\n')
                continue_trans = input('Would you like to make another transaction? Yes/No')

                if continue_trans == 'No':
                    sys.exit('\nThanks, have a great day!')
                elif continue_trans == 'Yes':
                    checkbook_app()
                else:
                    print('Not a vaild choice. Please type Yes or No.')

        if x == '4':
            print('\nThanks, have a great day!')
            
def create_checkbook_balance():
    filename = "checkbook_balance.txt"
    if os.path.isfile(filename):
        return filename
    else:
        with open('checkbook_balance.txt', 'w+') as balance:
            balance.write('0')

create_checkbook_balance()

checkbook_app()
