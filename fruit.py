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
    
    # Turtle initialization routine
    super(FruitTurtle,self).__init__(*args, **kwargs)

    # Initialize at position (x,y)
    self.penup()
    self.speed(0)
    self.hideturtle()
    self.goto(x, y)
    self.showturtle()
    self.setheading(-90)


  def initializeTextObject(self):
    
    # Save coordinates
    x = int(self.xcor())
    y = int(self.ycor())

    # Move text turtle to location
    Text.move(x=x, y=y)

    # Write text as Text
    Text.write(self.letter)
    
    # Move to previous coordinates
    # self.goto(x, y)
  

  def move(self, x:int=0, y:int=0, key:str=None):
    
    # Check for correct key pressed
    #if key == 
    

    # Move Apple
    self.goto(x, y)

    # Clear text as Text
    # self.clear()
    
    # Initialize at position (x,y)
    self.penup()
    self.speed(0)
    self.hideturtle()
    self.goto(x, y)

    # Write text as Text
    Text.write(self.letter)

    # Move Apple back to position after text as Text and reset image
    # self.goto(x-5, y+30)
    # self.image()

  
  def image(self):
    pass


class AppleTurtle (FruitTurtle):
  
  def __init__(self, *args, **kwargs):
    
    super(AppleTurtle,self).__init__(*args, **kwargs)
    
    self.image()

    super(AppleTurtle,self).initializeTextObject()
  
  def image(self):
    self.shape(FruitImages["Apple"])


class PearTurtle (FruitTurtle):
  
  def __init__(self, *args, **kwargs):
    
    super(PearTurtle,self).__init__(*args, **kwargs)
    
    self.shape(FruitImages["Pear"])

    super(PearTurtle,self).initializeTextObject()