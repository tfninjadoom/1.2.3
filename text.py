import turtle as TurtleModule

fontSetting = ("Arial", 30, "normal")

TextTurtle = TurtleModule.Turtle()
TextTurtle.hideturtle()
TextTurtle.penup()
TextTurtle.speed(0)

def move(x:int=0, y:int=0):
  TextTurtle.goto(x+2, y-28)

def write(text:str=""):
  TextTurtle.write(text, font=fontSetting, align="center")