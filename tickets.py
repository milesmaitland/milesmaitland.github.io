# Name: Miles Turner
# Prpg purpose: this is a program that finds the cost of movies tickets
# Price for one ticket: $10.99
# Sales Tax rate: 5.5%

import datetime

SALES_TAX_RATE = .055
PR_TICKET = 10.99

num_tickets = 0
subtotal = 0
sales_tax = 0
total = 0

def main():

    more_tickets = True 
    
    while more_tickets:
        get_user_data()
        perform_calculations()
        display results()
    
    yesno=input("\Would you like to order again (Y or N)")
    if yesno == "N" or yesno =="n"
        more_tickets = False
        print("Thank you for your order. Enjoy your movie!")

def get_user_data():
    global num_tickets
    num_tickets = int(input("Number of movie tickets: "))

def perform_calculations():
    global subtotal , sales_tax , total
    subtotal = num_tickets * PR_TICKET
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax

def display_results():
    print('-----------------------------')
    print('**** CINEMA HOUSE MOVIES ****')
    print('Your neighborhood movie house')
    print('-----------------------------')
    print('Tickets     $ ' +str(subtotal,'8,.2f'))
    print('Sales Tax   $ ' +str(sales_tax,'8,.2f'))
    print('Total       $ ' +str(total,'8,.2f'))
    print('-----------------------------')
    print(str(datetime.datetime.now()))

main()

\\