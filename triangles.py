import turtle

length = 300

def triangle():
    global length 
    turtle.forward(length)
    turtle.left(120)
    turtle.forward(length)
    turtle.left(120)
    turtle.forward(length)
    turtle.left(120)
  
def draw():
    global length 
    triangle()
    length = length/3
    triangle()
    length = length/3
    triangle()
draw()
    
                