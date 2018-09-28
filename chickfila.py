## Emma Stoverink
## Septmeber 25, 2018

## CONSTANTS
## BREAKFAST ITEMS
    # biscuit
BREAKFAST_ONE_NAME = "Chick-fil-A Chicken Biscuit"
BREAKFAST_ONE_PRICE = 3.49
    # bagel
BREAKFAST_TWO_NAME = "Chicken, Egg & Cheese Bagel"
BREAKFAST_TWO_PRICE = 3.69
    # burrito
BREAKFAST_THREE_NAME = "Hash Brown Scramble Burrito"
BREAKFAST_THREE_PRICE = 3.79
    # egg white grill
BREAKFAST_FOUR_NAME = "Egg White Grill"
BREAKFAST_FOUR_PRICE = 3.65
    # hash browns
BREAKFAST_FIVE_NAME = "Hash Browns"
BREAKFAST_FIVE_PRICE = 1.09
## LUNCH AND DINNER ITEMS
    # Chick-fil-A Chicken Sandwich
LUNCH_ONE_NAME = "Chick-fil-A Chicken Sandwich"
LUNCH_ONE_PRICE = 3.49
    # Spicy Chicken Sandwich
LUNCH_TWO_NAME = "Spicy Chicken Sandwich"
LUNCH_TWO_PRICE = 3.75
    #Grilled Chicken Sandwich
LUNCH_THREE_NAME = "Grilled Chicken Sandwich"
LUNCH_THREE_PRICE = 4.75
    # Waffle Fries
LUNCH_FOUR_NAME = "Waffle Fries"
LUNCH_FOUR_PRICE = 1.85
    # Milkshake
LUNCH_FIVE_NAME = "Milkshake"
LUNCH_FIVE_PRICE = 2.99

# OPENING WELCOME MENU
print("------------------------------------------------------------")
print("|{:^58}|".format("FSC Chick-fil-A Ordering System"))
print("------------------------------------------------------------")
print("| Please choose from the following menu:{:>20}".format("|"))
print("|\t1. Place a food order.{:>30}".format("|"))
print("|\t2. Nutritional information.{:>25}".format("|"))
print("|\t3. 3. Exit the Ordering System.{:>21}".format("|"))
welcome_choice = int(input("| Enter your choice: "))

# If the user wants to place a food order
if welcome_choice == 1:
    print("------------------------------------------------------------\n")
    print("---------------------Place a food order---------------------")
    print("Please choose from the following:")
    print("\tEnter \"Breakfast\" to place a breakfast order.")
    print("\tEnter \"Lunch\" to place a lunch order.")
    print("\tEnter \"Dinner\" to place a dinner order.")
    meal_choice = str(input("Enter your choice: ")).lower()
    # if the user wants to place a breakfast order
    if meal_choice == "breakfast":
        print("+---------------------> Breakfast Menu <--------------------+")
        print(" 1. {:<28}{:>28}".format(BREAKFAST_ONE_NAME,BREAKFAST_ONE_PRICE))
        print(" 2. {:<28}{:>28}".format(BREAKFAST_TWO_NAME,BREAKFAST_TWO_PRICE))
        print(" 3. {:<28}{:>28}".format(BREAKFAST_THREE_NAME,BREAKFAST_THREE_PRICE))
        print(" 4. {:<28}{:>28}".format(BREAKFAST_FOUR_NAME,BREAKFAST_FOUR_PRICE))
        print(" 5. {:<28}{:>28}".format(BREAKFAST_FIVE_NAME,BREAKFAST_FIVE_PRICE))
        print("------------------------------------------------------------\n")
    # if the user wants to place a lunch or dinner order
    elif meal_choice == "lunch" or meal_choice == "dinner":
        print("+---------------------> {} Menu <---------------------+".format(meal_choice.capitalize()))
        print(" 1. {:<28}{:>28}".format(LUNCH_ONE_NAME,LUNCH_ONE_PRICE))
        print(" 2. {:<28}{:>28}".format(LUNCH_TWO_NAME,LUNCH_TWO_PRICE))
        print(" 3. {:<28}{:>28}".format(LUNCH_THREE_NAME,LUNCH_THREE_PRICE))
        print(" 4. {:<28}{:>28}".format(LUNCH_FOUR_NAME,LUNCH_FOUR_PRICE))
        print(" 5. {:<28}{:>28}".format(LUNCH_FIVE_NAME,LUNCH_FIVE_PRICE))
        print("------------------------------------------------------------\n")
    else:
        print("\nInvalid meal selection given. Goodbye.")
    # Get the number of items they want and the number of each item they want
    meal_items = int(input("How many items do you want to order? (Enter 1, 2, or 3): "))
    if meal_items != 1 or meal_items != 2 or meal_items != 3:
        print("Invalid item selection. Goodbye.")
        exit()
    meal_choice1 = int(input("\tEnter the *number* of the 1st menu item you want: "))
    if meal_items >= 2:
        meal_choice2 = int(input("\tEnter the *number* of the 2nd menu item you want: "))
    if meal_items == 3:
        meal_choice3 = int(input("\tEnter the *number* of the 3rd menu item you want: "))

# If the user wants to view nutritional info
elif welcome_choice == 2:
    print("------------------------------------------------------------\n")
    print("------------------Nutritional Information-----------------")
    print("Please choose from the following:")
    print("\tEnter \"Breakfast\" to view breakfast nutritional info.")
    print("\tEnter \"Lunch\" to view lunch nutritional info.")
    print("\tEnter \"Dinner\" to view dinner nutritional info.")
    nutrition_choice = str(input("Enter your choice: ")).lower()

    # if the user wants to view breakfast nutrition info
    if nutrition_choice == "breakfast":
        print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("+---------------------> Breakfast Menu <--------------------+")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("{:<30}{:>29}".format("+","+"))
        print("+    1. Chick-fil-A Chicken Biscuit                       +")
        print("+    |  Calories|        Fat|      Carbs|    Protein|     +")
        print("+    |       440|        20g|        48g|        16g|     +")
        print("+   ---------------------------------------------------   +\n")
        print("+    2. Chicken, Egg & Cheese Bagel                       +")
        print("+    |  Calories|        Fat|      Carbs|    Protein|     +")
        print("+    |       460|        18g|        49g|        26g|     +")
        print("+   ---------------------------------------------------   +\n")
        print("+    3. Hash Brown Scramble Burrito                       +")
        print("+    |  Calories|        Fat|      Carbs|    Protein|     +")
        print("+    |       690|        38g|        52g|        35g|     +")
        print("+   ---------------------------------------------------   +\n")
        print("+    4.  Egg White Grill                                  +")
        print("+    |  Calories|        Fat|      Carbs|    Protein|     +")
        print("+    |       300|         7g|        31g|        25g|     +")
        print("+   ---------------------------------------------------   +\n")
        print("+    3.  Hash Browns                                      +")
        print("+    |  Calories|        Fat|      Carbs|    Protein|     +")
        print("+    |       250|        17g|        23g|         3g|     +")
        print("+   ---------------------------------------------------   +")
        print("{:<30}{:>29}".format("+","+"))
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    # if the user wants either lunch or dinner info
    elif nutrition_choice == "lunch" or nutrition_choice == "dinner":
        print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("+---------------------> {} Menu <---------------------+".format(nutrition_choice.capitalize()))
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("{:<30}{:>29}".format("+","+"))
        print("+    1. Chick-fil-A Chicken Sandwich                      +")
        print("+    |  Calories|        Fat|      Carbs|    Protein|     +")
        print("+    |       440|        19g|        40g|        28g|     +")
        print("+   ---------------------------------------------------   +\n")
        print("+    2.  Spicy Chicken Sandwich                           +")
        print("+    |  Calories|        Fat|      Carbs|    Protein|     +")
        print("+    |       450|        19g|        41g|        29g|     +")
        print("+   ---------------------------------------------------   +\n")
        print("+    3.  Grilled Chicken Sandwich                         +")
        print("+    |  Calories|        Fat|      Carbs|    Protein|     +")
        print("+    |       310|        6g|        36g|        29g|      +")
        print("+   ---------------------------------------------------   +\n")
        print("+    4.  Waffle Fries                                     +")
        print("+    |  Calories|        Fat|      Carbs|    Protein|     +")
        print("+    |       360|        18g|        43g|         5g|     +")
        print("+   ---------------------------------------------------   +\n")
        print("+    3.  Milkshake                                        +")
        print("+    |  Calories|        Fat|      Carbs|    Protein|     +")
        print("+    |       580|        22g|        88g|        12g|     +")
        print("+   ---------------------------------------------------   +")
        print("{:<30}{:>29}".format("+","+"))
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    # if neither of the options were selected
    else:
        print("\nInvalid meal selection given. Goodbye.")
# if the user did not choose one of the three options
else:
    print("------------------------------------------------------------\n")
    print("Invalid menu selection. Goodbye.")
