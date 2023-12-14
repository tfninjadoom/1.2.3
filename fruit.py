import turtle as TurtleModule
from random import choice
import Keys
import Text

# Storing image files in variables
FruitImages = { "Apple" : r"images\Apple.gif", "Pear" : r"images\Pear.gif" }


class FruitTurtle (TurtleModule.Turtle):
  """
  Fruit class that extends the Turtle class to have a letter attribute.
  """
  
  letter : str
  disabled = False

  def __init__(self, letter:str=None, x:int=0, y:int=0, *args, **kwargs):
    
    # Sets letter attribute if manually chosen
    self.letter = letter if (not letter==None) else choice(Keys.available)
    Keys.clickable.append(self.letter)
    #Keys.available.remove(self.letter)
    
    # Turtle initialization routine
    super(FruitTurtle,self).__init__(*args, **kwargs)

    # Initialize at position (x,y)
    self.penup()
    self.speed(0)
    self.hideturtle()
    self.goto(x, y)
    self.showturtle()
    self.setheading(-90)

    # Initialize fruit image
    self.image()

    # Initialize text object
    self.initializeTextObject()


  def initializeTextObject(self):
    
    # Save coordinates
    x = int(self.xcor())
    y = int(self.ycor())

    # Move text turtle to location
    self.moveText(x=x, y=y)

    # Write text as Text
    Text.write(self.letter)
  

  def move(self, x:int=0, y:int=0, key:str=None):

    # Clear Text
    Text.TextTurtle.clear()

    # Move Apple and Text
    self.goto(x, y)
    self.moveText(x, y)
    
    # Initialize at position (x,y)
    self.penup()
    self.speed(0)
    self.hideturtle()
    self.goto(x, y)

    # Write text as Text
    Text.write(self.letter)
  
  def image(self):
    pass

  def moveText(self, x:int, y:int):
    Text.move(x, y)


class AppleTurtle (FruitTurtle):
  
  def __init__(self, *args, **kwargs):
    
    super(AppleTurtle,self).__init__(*args, **kwargs)
  
  def image(self):
    self.shape(FruitImages["Apple"])
  
  def moveText(self, x:int, y:int):
    Text.move(x+2, y-28)


class PearTurtle (FruitTurtle):
  
  def __init__(self, *args, **kwargs):
    
    super(PearTurtle,self).__init__(*args, **kwargs)
  
  def image(self):
    self.shape(FruitImages["Pear"])
  
  def moveText(self, x:int, y:int):
    Text.move(x+1, y-37)