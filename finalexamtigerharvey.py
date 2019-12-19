#2019-20 Fall Computer Science Principles Final Exam

#Ms. Haubold


#Name
#Tiger Harvey
#Date
#12-19-2019
#

#### INSTRUCTIONS ####
#Create an etch a sketch turtle game
#The turtle should move with the arrow keys (up, down, left and right), and draw
#Space should clear the screen
#o and p should make the pen size bigger and smaller
#u should pick the pen up or put the pen down
#All code must be commented
#BONUS
#Add a feature to change colors
#

#import required libraries
import turtle as trtl


#create turtle

sketch = trtl.Turtle()
size = 5
shape = 'arrow' 
color= 'black'


#movement functions
def up():
    sketch.setheading(90)
    sketch.forward(10)

def down():
    sketch.setheading(-90)
    sketch.forward(10)

def right():
    sketch.setheading(0)
    sketch.forward(10)

def left():
    sketch.setheading(180)
    sketch.forward(10)


    




#color/drawing functions
#hides turtle
sketch.hideturtle()
sketch.pencolor('green')

#create screen
wn = trtl.Screen()
#bind to keypresses
wn.onkeypress(up, 'Up')
wn.onkeypress(down, 'Down')
wn.onkeypress(right, 'Right')
wn.onkeypress(left, 'Left')


#listen
wn.listen()

#mainloop
wn.mainloop()
