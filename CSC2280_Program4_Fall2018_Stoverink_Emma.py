# Emma Stoverink
# November 23, 2018
# emmajs16@live.com
# CSC 2280 LC1
# Program 4: FSC Clinic
# I will practice academic and personal integrity and excellence of character and expect the same from others.

import random
def display_main_menu():
    print("------------------------------------------------------")
    print("---        Welcome to the FSC Clinic System        ---")
    print("------------------------------------------------------")
    print("-    Enter \"Book\" for Booking Appointments           -")
    print("-    Enter \"Add\" for Adding Patients                 -")
    print("-    Enter \"Exit\" to Exit the Program                -")
    print("------------------------------------------------------")

def display_clinics_menu():
    print("------------------------------------------")
    print("---        Choose an FSC Clinic        ---")
    print("------------------------------------------")
    print("-    Enter G or g for General            -")
    print("-    Enter N or n for Nutrition          -")
    print("-    Enter S or s for Dermatology        -")
    print("-    Enter T or t for Dentistry          -")
    print("-    Enter R or r for previous menu      -")
    print("------------------------------------------")

def read_and_verify_main():
    while True:
        main_choice = str(input("Enter your Choice:")).lower()
        if main_choice == "book" or main_choice == "add" or main_choice == "exit":
            break
        print("Invalid selection. Please try again.")
    return main_choice.lower()


def read_and_verify_clinics():
    while True:
        clinic_choice = str(input("Enter your Choice:")).lower()
        if clinic_choice == "g" or clinic_choice == "n" or clinic_choice == "s" or clinic_choice == "t" or clinic_choice == "r":
            break
        print("Invalid selection. Please try again.")
    return clinic_choice.lower()

def compute_time(open_time, closing_time):
    appointment_time = random.randint(open_time,(closing_time+12))
    time_of_day = "AM"
    if appointment_time > 12:
        time_of_day = "PM"
        appointment_time -= 12
    return("{}:00 {}".format(appointment_time, time_of_day))


def print_booking(name, id, time, clinic, fee):
    print("               -------------------------------------------")
    print("                    Your New Booking is now Confirmed     ")
    print("               -------------------------------------------")
    print("NAME           :  {:<28}STUDENT ID NUMBER:  {}".format(name.upper(),id))
    print("CLINIC         :  {:<28}APPOINTMENT TIME:  {}".format(clinic,time))
    print("Appointment Fee:  {}".format(fee))

def compute_BMI(weight, height):
    # turn weight to kg
    weight = weight * 0.454
    # turn height to meters squared
    height = (height * 0.0254)**2
    bmi = weight / height
    if bmi <= 18.5:
        return("Underweight")
    elif bmi > 18.5 and bmi <=25:
        return("Normal")
    elif bmi >25 and bmi <=30:
        return("Overweight")
    elif bmi > 30:
        return("Obese")


def get_height():
    while True:
        height = int(input("Enter your height (in inches): "))
        if height > 36 or height < 96:
            break
        print("Invalid input. Please try again.")
    return height

def get_weight():
        while True:
            weight = int(input("Enter your weight (in pounds): "))
            if weight > 20 or weight < 800:
                break
            print("Invalid input. Please try again.")
        return weight

def get_age():
    while True:
        age = int(input("Enter your age (as a whole/integer number): "))
        if age > 0 or age > 110:
            break
        print("Invalid input. Please try again.")
    return age
def get_phone():
        while True:
            number = str(input("Enter your mobile number (###-###-####): "))
            if len(number)== 12:
                break
            print("Invalid input. Please try again.")
        return number
def add_patient_gt(name, id,age, phone, clinic):
    print("               -------------------------------------------")
    print("                 New Patient Details Added to the System  ")
    print("               -------------------------------------------")
    print("NAME           :  {:<28}STUDENT ID NUMBER:  {}".format(name.upper(),id))
    print("AGE            :  {:<28}PHONE NUMBER:  {}".format(age,phone))
    print("CLINIC         : {}".format(clinic))
    redirect()
def add_patient_n(name, id, age, phone, clinic, weight, height):
    print("               -------------------------------------------")
    print("                 New Patient Details Added to the System  ")
    print("               -------------------------------------------")
    print("NAME           :  {:<28}STUDENT ID NUMBER:  {}".format(name.upper(),id))
    print("AGE            :  {:<28}PHONE NUMBER:  {}".format(age,phone))
    print("CLINIC         :  {:<28}WEIGHT:  {}".format(clinic,weight))
    print("BMI            :  {:<28}HEIGHT:  {}".format(compute_BMI(weight, height),height))
    redirect()

def add_patient_s(name, id,age, phone, clinic, allergic):
    print("               -------------------------------------------")
    print("                 New Patient Details Added to the System  ")
    print("               -------------------------------------------")
    print("NAME           :  {:<28}STUDENT ID NUMBER:  {}".format(name.upper(),id))
    print("AGE            :  {:<28}PHONE NUMBER:  {}".format(age,phone))
    print("CLINIC         :  {:<28}".format(clinic))
    print("Allergies      :  {:<28}".format(allergic))
    redirect()

def redirect():
    print("--------------------------------------------------------------------------")
    print("-----> And you are now being redirected to the Main Menu...")
    print("--------------------------------------------------------------------------\n")

def main():
    while True:
        display_main_menu()
        choice_main = read_and_verify_main()
        if choice_main == "book":
            display_clinics_menu()
            choice_clinic = read_and_verify_clinics()
            if choice_clinic == "r":
                continue
            elif choice_clinic == "g":
                clinic = "GENERAL"
                open_time = 8
                closing_time = 5
                fee = "$10"
            elif choice_clinic == "t":
                clinic = "NUTRITION"
                open_time = 10
                closing_time = 2
                fee = "$5"
            elif choice_clinic == "n":
                clinic = "DERMATOLOGY"
                open_time = 10
                closing_time = 3
                fee = "$15"
            elif choice_clinic == "s":
                clinic = "DENTISTRY"
                open_time = 12
                closing_time = 4
                fee = "$20"
            name = str(input("Enter your name (first and then last): "))
            id = int(input("Enter your Student ID number:"))
            time = compute_time(open_time,closing_time)
            print("Your appointment will be at {}".format(time))
            cancel = int(input("Press 1 to confirm or 2 to cancel: "))
            if cancel == 2:
                continue
            else:
                print_booking(name,id, time,clinic, fee)

                # ADD
        elif choice_main == "add":
            display_clinics_menu()
            choice_clinic = read_and_verify_clinics()
            if choice_clinic == "g" or choice_clinic == "t":
                name = str(input("Enter your name (first and then last): "))
                id = int(input("Enter your Student ID number:"))
                age = get_age()
                phone = get_phone()
                if choice_clinic == "g":
                    clinic = "GENERAL"
                else:
                    clinic = "DENTISTRY"
                add_patient_gt(name, id, age, phone,clinic)
            elif choice_clinic == "n":
                name = str(input("Enter your name (first and then last): "))
                id = int(input("Enter your Student ID number:"))
                age = get_age()
                phone = get_phone()
                weight = get_weight()
                height = get_height()
                clinic = "NUTRITION"
                add_patient_n(name, id, age, phone,clinic, weight, height)
            elif choice_clinic == "s":
                name = str(input("Enter your name (first and then last): "))
                id = int(input("Enter your Student ID number:"))
                age = get_age()
                phone = get_phone()
                clinic = "DERMATOLOGY"
                allergic = str(input("Please enter any known allergies (on one line):"))
                add_patient_s(name, id, age, phone,clinic, allergic)

            elif choice_clinic == "r":
                continue
        else:
            print("Thank you for using the FSC Clinic System.")
            break

main()
