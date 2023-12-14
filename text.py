import turtle as TurtleModule


# Global Font Configuration
fontSetting = ("Arial", 30, "normal")

# TextTurtle Setup
TextTurtle = TurtleModule.Turtle()
TextTurtle.hideturtle()
TextTurtle.penup()
TextTurtle.speed(0)

# Move the TextTurtle to x, y
def move(x:int=0, y:int=0, xOffset:int=0, yOffset:int=0):
  TextTurtle.goto(x+xOffset, y+yOffset)

# Write text on screen with TextTurtle
def write(text:str):
  TextTurtle.write(text, font=fontSetting, align="center")