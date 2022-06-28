def turn_right():
    turn_left()
    turn_left()
    turn_left()

for wall in range(6):
    move()    
    turn_left()    
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
