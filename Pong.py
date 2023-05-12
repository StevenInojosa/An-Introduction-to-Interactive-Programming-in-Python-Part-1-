# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

ball_pos = [WIDTH / 2, HEIGHT / 2]
vel = [0, 0]
paddle1_pos = [[HALF_PAD_WIDTH, HEIGHT/2 - HALF_PAD_HEIGHT],[HALF_PAD_WIDTH, HEIGHT/2 + HALF_PAD_HEIGHT]]
paddle2_pos = [[WIDTH-HALF_PAD_WIDTH, HEIGHT/2 - HALF_PAD_HEIGHT],[WIDTH-HALF_PAD_WIDTH, HEIGHT/2 + HALF_PAD_HEIGHT]]

upper_paddle = HEIGHT+HALF_PAD_HEIGHT
lower_paddle = HEIGHT-HALF_PAD_HEIGHT
ball_vel = [0,0]

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    if direction is True:
        ball_vel = [random.randrange(int(120*0.02), int(240*0.02)), -random.randrange(int(60*0.02), int(180*0.02))]
    else:
        ball_vel = [-random.randrange(int(120*0.02), int(240*0.02)), -random.randrange(int(60*0.02), int(180*0.02))]
            
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    paddle1_pos = [[HALF_PAD_WIDTH, HEIGHT/2 - HALF_PAD_HEIGHT],[HALF_PAD_WIDTH, HEIGHT/2 + HALF_PAD_HEIGHT]]
    paddle2_pos = [[WIDTH-HALF_PAD_WIDTH, HEIGHT/2 - HALF_PAD_HEIGHT],[WIDTH-HALF_PAD_WIDTH, HEIGHT/2 + HALF_PAD_HEIGHT]]
    score1 = 0
    score2 = 0
    spawn_ball(RIGHT)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")    
    # update ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")  

    # Update ball position
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos[0][1] = min(max(paddle1_pos[0][1]+vel[0],0),HEIGHT-PAD_HEIGHT)
    paddle1_pos[1][1] = min(max(paddle1_pos[1][1]+vel[0],PAD_HEIGHT),HEIGHT)
    
    paddle2_pos[0][1] = min(max(paddle2_pos[0][1]+vel[1],0),HEIGHT-PAD_HEIGHT)
    paddle2_pos[1][1] = min(max(paddle2_pos[1][1]+vel[1],PAD_HEIGHT),HEIGHT)
    
    # draw paddles
    canvas.draw_line(paddle1_pos[0],paddle1_pos[1], PAD_WIDTH, 'white')
    canvas.draw_line(paddle2_pos[0],paddle2_pos[1], PAD_WIDTH, 'white')  
    
    # determine whether paddle and ball collide    
    if ball_pos[0] <= (PAD_WIDTH + BALL_RADIUS) : # Lado Izquierdo
        if  (ball_pos[1] >= paddle1_pos[0][1]) and (ball_pos[1] <= paddle1_pos[1][1]):
            ball_vel[0] = -1.1*ball_vel[0]
            ball_vel[1] = 1.1*ball_vel[1]
        else:
            score2 += 1
            spawn_ball(RIGHT)
            
    elif ball_pos[0] >= (WIDTH - (PAD_WIDTH + BALL_RADIUS)): # Lado Derecho
        if  (ball_pos[1] >= paddle2_pos[0][1]) and (ball_pos[1] <= paddle2_pos[1][1]):
            ball_vel[0] = -1.1*ball_vel[0]
            ball_vel[1] = 1.1*ball_vel[1]
            
        else:
            score1 += 1
            spawn_ball(LEFT)
            
    if (ball_pos[1] <= BALL_RADIUS) or (ball_pos[1] >= HEIGHT-BALL_RADIUS):
        ball_vel[1] = -ball_vel[1]  
                   
    # draw scores
    canvas.draw_text( str(score1), (150, 60), 50, 'white')
    canvas.draw_text( str(score2), (450, 60), 50, 'white')
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    
    spd = -2.2
    if key==simplegui.KEY_MAP["W"]:
        vel[0] = spd
    elif key==simplegui.KEY_MAP["S"]:
        vel[0] = -spd
    if key==simplegui.KEY_MAP["down"]:
        vel[1] = -spd
    elif key==simplegui.KEY_MAP["up"]:
        vel[1] = spd
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    
    if key==simplegui.KEY_MAP["W"]:
        vel[0] = 0
    elif key==simplegui.KEY_MAP["S"]:
        vel[0] = 0
    if key==simplegui.KEY_MAP["down"]:
        vel[1] = 0
    elif key==simplegui.KEY_MAP["up"]:
        vel[1] = 0
        
# define event handler for timer with 0.02 sec interval
def timer_handler():
    global time
    time += 0.02
    
def Reset() :
    global time, wins, attempts, score
    timer.stop()
    time = 0
    wins = 0
    attempts = 0
    score = str(0) + "/" + str(0)
 


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
timer = simplegui.create_timer(20, timer_handler)
button2 = frame.add_button('Reset', new_game ,130 )  

# start frame
new_game()
frame.start()
