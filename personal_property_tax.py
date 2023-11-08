import datetime 

TAX_RATE = 4.2
TAX_RELIEF_PERCENT = .33


def main():
    more = True 
    while more:
        get_tax_data()

        if eligible_relief () == "Y"
            get_tax_data()
            perform_calculations()
            display_results()

        if eligible_relief () == "N"
            get_tax_data()
            perform_calculations_n()
            display_results()


def get_tax_data():
    global eligible_relief , assesed_value
    eligible_relief = input ("Is your vehicle eligble for tax relief:(Y/N) ")
    assesed_value = int (input("What is your vehicles assesed value: "))

def perform_calculations():
    global full_tax , tax_relief , tax_due
    full_tax = assesed_value * TAX_RATE / 2
    tax_relief = full_tax * TAX_RELIEF_PERCENT
    tax_due = full_tax - tax_relief

def perform_calculations_n():
    full_tax = assesed_value * TAX_RATE / 2
    tax_relief = 0
    tax_due = full_tax - tax_relief


def display_results():
    print('-----------------------------')
    print('2023/2 Personal Property Tax*')
    print('-----------------------------')
    print('Assessed Value      $ ' +str(assesed_value,'8,.2f')))
    print('Full Tax Amount     $ ' +str(full_tax,'8,.2f'))
    print('Relief              $ ' +str(tax_relief,'8,.2f'))
    print('Tax Due             $ ' +str(tax_due,'8,.2f'))
    print('-----------------------------')
    print(str(datetime.datetime.now()))
