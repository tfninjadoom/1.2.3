import turtle as TurtleModule
import Fruit
from random import randint
import Keys
import Callback

# Initialization Code
Window = TurtleModule.Screen()
Window.setup(width=607, height=406)

BackgroundImage = r"images\Background.gif"
Window.addshape(BackgroundImage)
Window.bgpic(BackgroundImage)

for Image in Fruit.FruitImages.values(): Window.addshape(Image)

# Create an apple object from the AppleTurtle class
AppleObject = Fruit.AppleTurtle( x=randint(-150,150), y=randint(-40,120) )
Window.update()

# Callback Function to Key Presses
Callback.KeyPressCallBacks()
Window.mainloop()