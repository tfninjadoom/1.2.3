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
TurtleModule.screensize(canvwidth=607, canvheight=406)

BackgroundImage = r"images\Background.gif"
Window.addshape(BackgroundImage)
Window.bgpic(BackgroundImage)

for Image in Fruit.FruitImages.values(): Window.addshape(Image)

FruitObjects = []
FruitNum = 5

###---------- FUNCTIONS ----------###

# Create an Fruit object from the FruitTurtle class
def NewFruit(i:int=0):
  global FruitObjects

  # Randomly choose between Apple and Pear
  fruitType = RChoice(["Apple", "Pear"])
  match (fruitType):
    case "Apple":
      FruitObjects[i] = Fruit.AppleTurtle( x=Random(-150,150), y=Random(-40,120), i=i)
    case "Pear":
      FruitObjects[i] = Fruit.PearTurtle( x=Random(-150,150), y=Random(-40,120), i=i)

  Window.update()

# When Letter Key Pressed
def KeyPress(letter:str):

  # If Correct Letter
  if letter in Keys.clickable:
    for i, FruitObject in enumerate(FruitObjects):
      if FruitObject.letter == letter:
        # Reward User
        print(f"Great Work! ({letter})")
        Keys.clickable.remove(letter)

        # Move the Fruit to floor and clear its letter
        FruitObject.speed(5)
        FruitObject.move(FruitObject.xcor,-160)
        Text.clear(i)

        # Create a New Fruit
        NewFruit(i)
    
    # Respawn letters of remaining Fruits
    for i, FruitObject in enumerate(FruitObjects):
      x = FruitObject.xcor
      y = FruitObject.ycor
      FruitObject.moveText(x, y, i)
      Text.write(FruitObject.letter, i)

  # Else Incorrect
  else:
    print(f"Try Again! ({letter})")


###---------- PROGRAM BODY ----------###

# Create Initial Starting Fruit and Text
for i in range(FruitNum):
  Placeholder1 = TurtleModule.Turtle()
  Placeholder2 = TurtleModule.Turtle()
  Placeholder1.penup()
  Placeholder1.hideturtle()
  Placeholder2.penup()
  Placeholder2.hideturtle()
  FruitObjects.append(Placeholder1)
  Text.TextTurtles.append(Placeholder2)
  NewFruit(i)
  Text.Setup(i)
  del Placeholder1, Placeholder2

# Callback Functions for Key Presses
for letter in Keys.available:
  Window.onkeypress(
    lambda key=letter: KeyPress(key) ,
    letter
    )

# Game Loop
Window.listen()
Window.mainloop()