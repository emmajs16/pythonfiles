# CAR COMPANY DISPLAY NAMES FUNCTIONS
def companies():
    print("\n     ------- COMPANIES -------")
    print("-----------------------------------")
    print(" | T or t : Toyota               | ")
    print(" | C or c : Chevrolet            | ")
    print(" | H or h : Honda                | ")
    print(" | K or k : Kia                  | ")
    print(" | R or r : Return to Main Menu  | ")
    print("-----------------------------------")
    global company_choice
    company_choice = str(input("Please enter your choice: ")).lower()

def toyota():
    print("\n      ------- VEHICLES -------")
    print("-------------------------------------")
    print(" | C or c:  Corolla 2018           | ")
    print(" | M or m:  Camry 2018             | ")
    print(" | V or v:  Rav4 2018              | ")
    print(" | R or r:  Previous Menu          | ")
    print(" ----------------------------------- ")
    global car_choice
    car_choice = str(input("Please enter your choice: ")).lower()

def chevrolet():
    print("\n      ------- VEHICLES -------")
    print("-------------------------------------")
    print(" | C or c:  Cruze 2018             | ")
    print(" | M or m:  Malibu 2018            | ")
    print(" | V or v:  Corvette 2018          | ")
    print(" | R or r:  Previous Menu          | ")
    print(" ----------------------------------- ")
    global car_choice
    car_choice = str(input("Please enter your choice: ")).lower()

def honda():
    print("\n      ------- VEHICLES -------")
    print("-------------------------------------")
    print(" | C or c:  Civic 2018             | ")
    print(" | A or a:  Accord 2018            | ")
    print(" | V or v:  CR-V 2018              | ")
    print(" | R or r:  Previous Menu          | ")
    print(" ----------------------------------- ")
    global car_choice
    car_choice = str(input("Please enter your choice: ")).lower()

def kia():
    print("\n      ------- VEHICLES -------")
    print("-------------------------------------")
    print(" | F or f:  Forte 2018             | ")
    print(" | O or o:  Optima 2018            | ")
    print(" | N or n:  Niro 2018              | ")
    print(" | R or r:  Previous Menu          | ")
    print(" ----------------------------------- ")
    global car_choice
    car_choice = str(input("Please enter your choice: ")).lower()












# MAIN FUNCTION
def main():
    while True:
        # main menu
        print("----------------------------------------------------------------------------------")
        print("-------           Welcome to Lakeland AUTOMALL Customer e-Portal           -------")
        print("----------------------------------------------------------------------------------")
        print("| 1 : Get information about the vehicles available for sale                      |")
        print("| 2 : Make appointments for different types of services (sales or maintenance)   |")
        print("| 3 : Submit customer feedback or complaint                                      |")
        print("| 4 : Exit                                                                       |")
        print("----------------------------------------------------------------------------------")
        main_choice = int(input("Please enter your choice: "))
        if main_choice == 1:
            while True:
                #VEHICLE INFO
                #display company options
                companies()
                if company_choice == "r":
                    break
                elif company_choice == "t":
                    #display toyota car types
                    while True:
                        toyota()
                        # display the information for the chosen car
                        if car_choice == "r":
                            break
                        elif car_choice == "c":
                            print("\n2018 Toyota Corolla")
                            print("Price: $17,600.00")
                            print("Quantity Available: 252")
                        elif car_choice == "m":
                            print("\n2018 Toyota Camry")
                            print("Price: $21,995.00")
                            print("Quantity Available: 250")
                        elif car_choice == "v":
                            print("\n2018 Toyota Rav4 2018")
                            print("Price: $23,895.00")
                            print("Quantity Available: 157")
                        else:
                            print("\nInvalid selection. Please try again.")
                elif company_choice == "c":
                    #display chevrolet car types
                    chevrolet()
                    # display the information for the chosen car
                    if car_choice == "r":
                        break
                    elif car_choice == "c":
                        print("\n2018 Chevrolet Cruze")
                        print("Price: $15,995.00")
                        print("Quantity Available: 28")
                    elif car_choice == "m":
                        print("\n2018 Chevrolet Malibu")
                        print("Price: $18,995.00")
                        print("Quantity Available: 25")
                    elif car_choice == "v":
                        print("\n2018 Chevrolet Corvette")
                        print("Price: $49,995.00")
                        print("Quantity Available: 30")
                    else:
                        print("\nInvalid selection. Please try again.")
                elif company_choice == "h":
                    # display honda car types
                    honda()
                    # display the information for the chosen car
                    if car_choice == "r":
                        break
                    elif car_choice == "c":
                        print("\n2018 Honda Civic")
                        print("Price: $17,795.00")
                        print("Quantity Available: 11")
                    elif car_choice == "a":
                        print("\n2018 Honda Accord")
                        print("Price: $22,295.00")
                        print("Quantity Available: 35")
                    elif car_choice == "v":
                        print("\n2018 Honda CR-V")
                        print("Price: $23,495.00")
                        print("Quantity Available: 12")
                    else:
                        print("\nInvalid selection. Please try again.")
                elif company_choice == "k":
                    # display kia car types
                    kia()
                    # display the information for the chosen car
                    if car_choice == "r":
                        break
                    elif car_choice == "f":
                        print("\n2018 Kia Forte")
                        print("Price: $15,790.00")
                        print("Quantity Available: 16")
                    elif car_choice == "o":
                        print("\n2018 Kia Optima")
                        print("Price: $20,790.00")
                        print("Quantity Available: 45")
                    elif car_choice == "n":
                        print("\n2018 Kia Niro")
                        print("Price: $21,690.00")
                        print("Quantity Available: 6")
                    else:
                        print("\nInvalid selection. Please try again.")
        elif main_choice == 2:
            while True:
                print("\n  ------ APPOINTMENT TYPE ------")
                print("-------------------------------------")
                print(" | 1: Service Appointment           |")
                print(" | 2: Sales Appointment             |")
                print(" | 3: Previous Menu                 |")
                print("-------------------------------------")
                appointment_choice = int(input("Please enter the choice:"))
                # display companies
                companies()
                # sets the company to the chosen company
                if company_choice == "t":
                    company = "TOYOTA"
                elif company_choice == "c":
                    company = "CHEVROLET"
                elif company_choice == "h":
                    company = "HONDA"
                elif company_choice == "k":
                    company = "KIA"
                elif company_choice == "r":
                    break
                else:
                    print("\nInvalid selection. Please try again.")
                # displays the form for the service appointment request
                if appointment_choice == 1:
                    name = str(input("\nEnter your name (first and last): "))
                    phone = str(input("Enter your mobile (###-###-####):"))
                    vehicle_model = str(input("Enter vehicle model: "))
                    mileage = int(input("Enter mileage: "))
                    description = str(input("Enter service description: "))
                    appointment_time = str(input("When do you want your service appointment: "))
                    print("\n-------------------------------------------------------------------------------------")
                    print(" | Yor request was received; you will be contacted within 24 hours to finalize it. |")
                    print("-------------------------------------------------------------------------------------")
                    # displays the confirmation to the service request
                    print("Here is a confirmation of your request to {}:".format(company))
                    print("\tAppointment Type: Service")
                    print("\tName: {}                                  Phone: {}".format(name,phone))
                    print("\tModel of your vehicle: {}".format(vehicle_model))
                    print("\tMileage: {}".format(mileage))
                    print("\tService Needed: {}".format(description))
                    print("\tPreferred date for Service appointment: {}".format(appointment_time))
                    print("\n**You will now be returned to the Appointment Menu.")
                elif appointment_choice == 2:
                    name = str(input("\nEnter your name (first and last): "))
                    phone = str(input("Enter your mobile (###-###-####):"))
                    vehicle_model = str(input("Which vehicle are you interested in: "))
                    num_vehicles = int(input("How many vehicles are you wanting to purchase: "))
                    appointment_time = str(input("When do you want your sales appointment: "))
                    print("\n-------------------------------------------------------------------------------------")
                    print(" | Yor request was received; you will be contacted within 24 hours to finalize it. |")
                    print("-------------------------------------------------------------------------------------")
                    # displays the confirmation to the service request
                    print("Here is a confirmation of your request to {}:".format(company))
                    print("\tAppointment Type: Sales")
                    print("\tName: {}                                  Phone: {}".format(name,phone))
                    print("\tModel of vehicle you are interested in: {}".format(vehicle_model))
                    print("\tNumber of vehicles planning to purchase: {}".format(num_vehicles))
                    print("\tPreferred date for Sales appointment: {}".format(appointment_time))
                    print("\n**You will now be returned to the Appointment Menu.")
                elif appintment_choice == 3:
                    break
                else:
                    print("\nInvalid selection. Please try again.")
            else:
                print("\nInvalid selection. Please try again.")
main()
