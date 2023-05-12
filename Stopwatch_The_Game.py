# template for "Stopwatch: The Game"

import simplegui
import math

# define global variables
time = 0
wins = 0
attempts = 0
score = str(0) + "/" + str(0) 

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(time):
    d4 = int(10*(time - math.floor(time)))
    d3 = int(time%10)
    d2 = int(((time%100-time%10))/10)%6
    d1 = int(math.floor( time/60 ))
    return str(d1) + ":" + str(d2) + str(d3) + "." + str(d4)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def Start() :
    timer.start()
        
def Stop() :
    global wins, attempts, score
    timer.stop()
    if int(10*(time - math.floor(time))) == 0:
        wins += 1
    attempts += 1
    score = str(wins) + "/" + str(attempts) 
    
    
    
def Reset() :
    global time, wins, attempts, score
    timer.stop()
    time = 0
    wins = 0
    attempts = 0
    score = str(0) + "/" + str(0)

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global time
    time += 0.1
        
# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(time), (130, 220), 80, 'White')
    canvas.draw_text(score, (335, 35), 30, 'White')    
   
    
    
# create frame
frame = simplegui.create_frame('Stopwatch: The game', 400, 400)

# register event handlers
button0 = frame.add_button('Start', Start,130 )
button1 = frame.add_button('Stop ', Stop,130 )
button2 = frame.add_button('Reset', Reset,130 )

frame.set_draw_handler(draw_handler)
timer = simplegui.create_timer(100, timer_handler)

# start frame
frame.start()


# Please remember to review the grading rubric
