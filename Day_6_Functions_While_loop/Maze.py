def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while front_is_clear():
    move()
turn_right()

while not at_goal():
    
    if not wall_on_right():
            turn_right()
            move()
    else :
        turn_left()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
