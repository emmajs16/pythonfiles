# Emma Stoverink
# November 2, 2018
# Menu-driven Nested Loops

while True:
    # main menu
    print()
    print("Main menu: Choose an option")
    print("\t1 - go to inner ABR menu")
    print("\t2 - go to inner XYR menu")
    print("\t3 - to exit")
    main_choice = eval(input("Enter your choice (1, 2,or 3): "))
    if main_choice == 1:
        # ABR menu
        while True:
            print()
            print("ABR Menu: Choose an option")
            print("\tA")
            print("\tB")
            print("\tR (return to previous menu)")
            abr_choice = str(input("Enter your choice: ")).upper()
            if abr_choice != "A" and abr_choice != "B" and abr_choice != "R":
                print("\nInvalid selection --- Try again.")
            elif abr_choice == "R":
                break
            else:
                print("\nYou chose \"{}\".".format(abr_choice))
    if main_choice == 2:
        # XYR menu
        while True:
            print()
            print("XYR Menu: Choose an option")
            print("\tX")
            print("\tY")
            print("\tR (return to previous menu)")
            xyr_choice = str(input("Enter your choice: ")).upper()
            if xyr_choice != "X" and xyr_choice != "Y" and xyr_choice != "R":
                print("\nInvalid selection --- Try again.")
            elif xyr_choice == "R":
                break
            else:
                print("\nYou chose \"{}\".".format(xyr_choice))
    # exit
    if main_choice == 3:
        break
    # if the choice is invalid or the wrong data type
    if main_choice != 1 and main_choice != 2 and main_choice != 3:
        print("\nInvalid selection --- Try again.")
        if isinstance(main_choice,int) == False:
            print("(You must enter a digit.)")
    