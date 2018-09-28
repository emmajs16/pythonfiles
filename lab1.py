#Emma Stoverink
#August 31, 2018
#Lab 1

#display three messages
def problem_one():
    print("Welcome to Python")
    print("Welcome to Computer Science")
    print("Programming is fun")
#displays message five times
def problem_two():
    for i in range(5):
        print("Welcome to Python")

#Display a pattern that prints out the word FUN
def problem_three():
    print("FFFFFFF     U       U       NN     NN")
    print("FF          U       U       NNN    NN")
    print("FFFFFF      U       U       NN  N  NN")
    print("FF           U     U        NN   N NN")
    print("FF             UUU          NN    NNN")
    
#Prints a table of values
def problem_four():
    print("a\ta^2\ta^3")
    print("1\t1\t1")
    print("2\t4\t8")
    print("3\t9\t27")
    print("4\t16\t64")

#Computes an expression
def problem_five():
    numerator = (9.5 * 4.5) - (2.5 *3)
    denominator = 45.5 - 3.5
    print(numerator /denominator)

def problem_six():
    mile_in_km = 1.6
    distance = 14
    time= 45.5
    hour = 60

    scale = time / hour
    distance_in_miles = distance / mile_in_km

    print(scale * distance_in_miles)
    print("MPH")

#display 3d box
def problem_seven():
    #make first rectangle
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(100)
    #make line to connect
    turtle.left(180)
    turtle.right(45)
    turtle.forward(100)
    turtle.left(45)
    turtle.right(90)
    #make second rectangle
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(100)
    #connect the last two lines
    turtle.right(180)
    turtle.forward(100)
    turtle.left(135)
    turtle.forward(100)

    turtle.left(45)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(45)
    turtle.forward(100)

    turtle.left(45)
    turtle.forward(100)
    turtle.left(135)
    turtle.forward(100)
