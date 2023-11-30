import turtle as TurtleModule
from fruit import AppleTurtle, PearTurtle, FruitImages
from random import randint

# Initialization Code
Window = TurtleModule.Screen()
Window.setup(width=607, height=406)

BackgroundImage = r"Background.gif"
Window.addshape(BackgroundImage)
Window.bgpic(BackgroundImage)

for Image in FruitImages.values(): Window.addshape(Image)

# Functions
def DrawApple(CurrentApple):
  Window.update()

# Create an apple object from the AppleTurtle class
AppleObject = AppleTurtle( x=randint(-150,150), y=randint(-40,120) )

# Function Calls
DrawApple(AppleObject)


# Callback Function to Key Presses
Window.onkey( key="a", fun=AppleObject.move() ,)
Window.mainloop()