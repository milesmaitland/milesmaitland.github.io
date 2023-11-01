# Name: Miles Turner
# Prog purpose : animal vaccine

import datetime

PR_BORD = 30
PR_DAPP = 35
PR_FLU = 48

PR_ALL = 0

PR_CHEWS_SMALL = 9.99
PR_CHEWS_MED = 11.99
PR_CHEWS_LARGE = 13.99

def main():
    more = True 
    while more:
        get_user_data()

        if pet_type.upper() == "D"
            get_dog_data()
            perform_dog_calculations()
            diplay_dog_results()
        else:
            get_cat_data()
            perform_cat_calculations()
            display_cat_results()
        
        askAgain = input ("\nWould you like process another pet (Y/N): ")
        if askAgain.upper() == "N" :
            more = False
            print('Thank you for trusting PET CARE MEDS with your pet vaccines and medications')

def get_user_data():
    global pet_name , pet_type , pet_weight
    pet_name = input ("Pet name: ")
    pet_type = input ('Is this pet a dog(D) or cat(C)')
    pet_weight = int(input("Weight of your pet(in pounds)"))

def get_dog_data():
    global pet_vax_type, num_chews
    dog1 = "\n** Dog vaccines: \n\t1.Bordatella \n\t2.DAPP \n\t3.Influenza \n4.Leptospirosis"
    dog2 = "\n\t5.Lyme Disease \n\t6.Rabies \n\t7.Full Vaccine Package \n\t8.NONE"
    dogmenu = dog1 + dog2
    pet_vax_type = int(input(dogmenu + "\n** Enter Vaccine number"))

    print("\nMonthly heart worm prevention medication is reccommended for all dogs")
    heart_yesno = input("\nWould you like to order monthly heartworm medication for " + pet_name + " (Y/N)? ")
    if heart_yesno.upper() == "Y":
        num_chews = int(input("\tHow many heart worm chews would you like to order?"))
    