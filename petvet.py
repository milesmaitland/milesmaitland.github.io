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

def perform_dog_calculations() :
    global vax_cost , vax_name , chews_cost , total

    if pet_vax_type == 1 :
        vax_cost = PR_BORD
        vax_name = "Bordatella"
    elif pet_vax_type == 2
        vax_cost = PR_DAPP
        vax_name = "DAPP"
    elif pet_vax_type == 3
        vax_cost = PR_FLU
        vax_name = "Influenza"
    else: 
        PR_ALL = PR_BORD + PR_DAPP + PR_FLU
        vax_cost = .85 * PR_ALL
        vax_name = "Full Vax Package"

if num_chews ! =0:
    if pet_weight < 25:
        chews_cost = num_chews * PR_CHEWS_SMALL

elif pet_weight >= 26 and pet_weight < 50:
    chews_cost = num_chews * PR_CHEWS_LARGE

total = vax_cost + chews_cost

def display_dog_results() :
    print ("DISPLAY DOGS")

def get_cat_data():
    print ("CAT CALCS")

def perform_cat_calculations():
    print ("CAT CALCS")

def display_cat_results():
    print("DISPLAY CATS")

main()

    
