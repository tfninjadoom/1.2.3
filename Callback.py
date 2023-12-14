import Keys

def KeyPressCallBacks():
  for letter in Keys.available:
    import Main        
    Main.Window.onkey( key=letter, fun=Main.AppleObject.move() )
