import turtle as t

# Set up the screen
t.setup(600,600,10,70)
t.tracer(False)
t.bgcolor("pink")
t.hideturtle()
t.title(" tic- tac-toe")
# Draw horizontal lines and vertical lines to froooom grid
t.pensize(10)                     
for i in (-100,100):
    t.up()
    t.goto(i,-300)
    t.down()
    t.goto(i,300)
    t.up()
    t.goto(-300,i)
    t.down()
    t.goto(300,i)
    t.up()
# create a dictionary to map cell numbers to cell center coordinates
cellcenter = {'1':(-200,-200), '2':(0,-200), '3':(200,-200),
              '4':(-200,0), '5':(0,0), '6':(200,0),
              '7':(-200,200), '8':(0,200), '9':(200,200)}
# Go to center of each cell, write down the cell number
