import turtle as TurtleModule
from random import choice
import keys

# Storing image files in variables
AppleImage = r"Apple.gif"
PearImage = r"Pear.gif"
FruitImages = [AppleImage, PearImage]


class FruitTurtle (TurtleModule.Turtle):
  """
  Fruit class that extends the Turtle class to have a letter attribute.
  """
  
  letter : str
  textObject : TurtleModule.Turtle
  disabled = False

  def __init__(self, letter:str=None, x:int=0, y:int=0, *args, **kwargs):
    
    # Sets letter attribute if manually chosen
    self.letter = letter if (not letter==None) else choice(keys.available)
    keys.clickable.append(self.letter)
    
    # Turtle initialization routine
    super(FruitTurtle,self).__init__(*args, **kwargs)

    # Initialize at position (x,y)
    self.penup()
    self.speed(0)
    self.hideturtle()
    self.goto(x, y)
    self.showturtle()
    self.setheading(-90)

    self.initializeTextObject()

  def move(self, x:int =0, y:int =0):
    self.goto(x, y)
    self.textObject.clear()
    self.textObject.goto(x, y)
    self.textObject.write( 'a' )


  def initializeTextObject(self):
    self.textObject = TurtleModule.Turtle()
    
    # Initialize at position (x,y)
    self.textObject.penup()
    self.textObject.speed(0)
    self.textObject.hideturtle()
    self.textObject.goto(self.xcor, self.ycor)

    # Write tpyext
    self.textObject.write('a')



class AppleTurtle (FruitTurtle):
  
  def __init__(self, *args, **kwargs):
    
    super(AppleTurtle,self).__init__(*args, **kwargs)
    
    self.shape(AppleImage)


class PearTurtle (FruitTurtle):
  
  def __init__(self, *args, **kwargs):
    
    super(PearTurtle,self).__init__(*args, **kwargs)
    
    self.shape(PearImage)