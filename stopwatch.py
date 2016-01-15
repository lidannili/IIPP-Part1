# template for "Stopwatch: The Game"
import simplegui

# define global variables

width = 150
height = 150
interval=100

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
# t is in 0.1 seconds
# A:BC.D
A=0
B=0
C=0
D=0
win = 0
trial = 0
#time = str(A) + ":" + str(B)+str(C) + "." + str(D)
 
def format(t):    
    global A
    global B
    global C
    global D    
    if t< 600:
        B= (t-600*(t/600) )/100
        C= ((t-600*(t/600) )%100-(t-600*(t/600) )%10)/10
        D= (t-600*(t/600) )%10
        return str(A) + ":" + str(B)+str(C) + "." + str(D)
    else:
        A = A+t/600
        B= (t-600*(t/600) )/100
        C= ((t-600*(t/600) )%100-(t-600*(t/600) )%10)/10
        D= (t-600*(t/600) )%10
        return str(A) + ":" + str(B)+str(C) + "." + str(D)

       
# define event handlers for buttons; "Start", "Stop", "Reset"
def Start():
    global trial
    if not timer.is_running():
        trial = trial + 1
    timer.start()
        
def Stop():
    global win
    if timer.is_running() and D==0:
        win = win + 1
    timer.stop()
def Reset():
    global time
    global win
    global trial
    timer.stop()
    time = 0
    win = 0
    trial = 0
    

# define event handler for timer with 0.1 sec interval
time = 0
def timer_handler():
    global time
    time=time+1
        
# define draw handler
def draw(canvas):
    canvas.draw_text(format(time), [80,150], 60, "White")
    canvas.draw_text("player :"+ str(win) + "/" + str(trial),[200,50],20,"Red")
    
# create frame
frame = simplegui.create_frame("Home", 300, 300)
timer = simplegui.create_timer(interval,timer_handler)

# register event handlers
frame.set_draw_handler(draw)
frame.add_button("Start", Start, 100)
frame.add_button("Stop", Stop, 100)
frame.add_button("Reset", Reset, 100)


# start frame
frame.start()

# Please remember to review the grading rubric
