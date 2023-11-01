# Name: Miles Turner
# Prpg purpose: branch bbq buffet 
# Price for an adult meal: 19.95
# Price for a child meal: 11.95
# Service fee rate: 10%
# Sales Tax rate: 6.2%

import datetime

SALES_TAX_RATE = .062
PR_ADULT = 19.95
PR_CHILD = 11.95
SERVICE_FEE = .10

adult meals = 0
child meals = 0
subtotal = 0
service_fee = 0
sales_tax = 0
total = 0

def main():

    more_meals = True 
    
    while more_meals:
        get_user_data()
        perform_calculations()
        display results()
    
    yesno=input("\Would you like to order again (Y or N)")
    if yesno == "N" or yesno =="n"
        more_tickets = False
        print("Thank you for your order. Enjoy your meal!")

def get_user_data():
    global num_adults_meals
    global num_child_meals
    num_adults_meals = int(input("Number of Adult meals: "))
    num_child_meals = int(input("Number of Child meals: "))

def perform_calculations():
    global subtotal , sales_tax , total
    subtotal = num_adult meals * PR_ADULT + num_child_meals * PR_CHILD
    sales_tax = subtotal * SALES_TAX_RATE
    service_fee = subtotal * SERVICE_FEE
    total = subtotal + sales_tax + service_fee

def display_results():
    print('-----------------------------')
    print('****  Branch BBQ Buffet  ****')
    print(' Your neighborhood Barbeque  ')
    print('-----------------------------')
    print('Tickets     $ ' +str(subtotal,'8,.2f'))
    print('Sales Tax   $ ' +str(sales_tax,'8,.2f'))
    print('Total       $ ' +str(total,'8,.2f'))
    print('-----------------------------')
    print(str(datetime.datetime.now()))

main()