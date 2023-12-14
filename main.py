import turtle as TurtleModule
from random import randint as Random
from random import choice as RChoice
import Fruit
import Keys
import Text

###---------- SETUP ----------###

# Initialization Code
Window = TurtleModule.Screen()
Window.setup(width=607, height=406)

BackgroundImage = r"images\Background.gif"
Window.addshape(BackgroundImage)
Window.bgpic(BackgroundImage)

for Image in Fruit.FruitImages.values(): Window.addshape(Image)

FruitObject : Fruit.FruitTurtle

###---------- FUNCTIONS ----------###

# Create an Fruit object from the FruitTurtle class
def NewFruit():
  global FruitObject

  # Randomly choose between Apple and Pear
  fruitType = RChoice(["Apple", "Pear"])
  match (fruitType):
    case "Apple":
      FruitObject = Fruit.AppleTurtle( x=Random(-150,150), y=Random(-40,120) )
    case "Pear":
      FruitObject = Fruit.PearTurtle( x=Random(-150,150), y=Random(-40,120) )

  Window.update()

# When Letter Key Pressed
def KeyPress(letter:str):

  # If Correct Letter
  if letter in Keys.clickable:
    
    # Reward User
    print(f"Great Work! ({letter})")
    Keys.clickable.remove(letter)

    # Move the Fruit to floor and clear its letter
    x = FruitObject.xcor()
    FruitObject.speed(5)
    FruitObject.move(x,-160)
    Text.TextTurtle.clear()

    # Create a New Fruit
    NewFruit()

  # Else Incorrect
  else:
    print(f"Try Again! ({letter})")


###---------- PROGRAM BODY ----------###

# Create Initial Starting Fruit
NewFruit()

# Callback Functions for Key Presses
for letter in Keys.available:
  Window.onkeypress(
    lambda key=letter: KeyPress(key) ,
    letter
    )

# Game Loop
Window.listen()
Window.mainloop()