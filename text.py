import turtle as TurtleModule

# Global Configuration
fontSetting = ("Arial", 30, "normal")

TextTurtles = []

# TextTurtles Setup
def Setup(i):
  global TextTurtles
  TextTurtles[i] = TurtleModule.Turtle()
  TextTurtles[i].hideturtle()
  TextTurtles[i].penup()
  TextTurtles[i].speed(0)

# Move the TextTurtle to x, y
def move(x:int=0, y:int=0, xOffset:int=0, yOffset:int=0, i:int=0):
  global TextTurtles
  TextTurtles[i].goto(x+xOffset, y+yOffset)

# Write text on screen with TextTurtle
def write(text:str, i:int=0):
  global TextTurtles
  TextTurtles[i].write(text, font=fontSetting, align="center")

def clear(i:int=0):
  global TextTurtles
  TextTurtles[i].clear()