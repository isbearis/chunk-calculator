
# This algorithm calculates the chunks of spiral
# using x , y and step variables

# The calculated spiral starts from center and goes to clockwise direction.

x , y = 0 , 0
# xydist is the distance between each chunk (symetric)
xydist = 150
step = 1

def calculate_spiral_chunk(x: int = 0 , y: int = 0 , step: int = 1):
    
    next_step = 2 * step
    if x == -xydist * (next_step - step) and y == xydist * (next_step - step): step += 1
    next_step = 2 * step
    
    if x == 0 and y == 0 : x = x; y += xydist # INITALIZE UP
    elif (x <= 0 or x != xydist * (next_step - step)) and y == xydist * (next_step - step): x += xydist; y = y; # RIGHT
    elif x != -xydist * (next_step - step) and y == -xydist * (next_step - step): x -= xydist; y = y; # LEFT
    elif x == xydist * (next_step - step) and y != -xydist * (next_step - step): x = x; y -= xydist; # DOWN
    elif x != -xydist * next_step and y != xydist * (next_step - step): x = x; y += xydist # UP

    
    print(x,y,step)
    #return (x,y,step)

calculate_spiral_chunk(x,y,step)
