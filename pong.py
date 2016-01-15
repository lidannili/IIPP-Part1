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
paddle1_pos = HEIGHT/2-HALF_PAD_HEIGHT
paddle2_pos = HEIGHT/2-HALF_PAD_HEIGHT
paddle1_vel=0
paddle2_vel=0
score1=0
score2=0
    
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left

ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0, 0]
#spawn_ball(direction)
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    if direction==RIGHT:
        ball_vel[0] = random.randrange(120/60,240/60)
        ball_vel[1] = -random.randrange(60/60,180/60)
    elif direction == LEFT:
        ball_vel[0] = -random.randrange(120/60,240/60)
        ball_vel[1] = -random.randrange(60/60,180/60)
    
    ball_pos[0]+= ball_vel[0]     
    ball_pos[1]+= ball_vel[1]
    
# define event handlers
def Restart():
    global ball_pos
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    new_game()
    
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    #if ball_pos[1] <= BALL_RADIUS:
        #ball_vel[1] = -ball_vel[1]
    #elif ball_pos[1] >=HEIGHT-BALL_RADIUS:
        #ball_vel[1] = -ball_vel[1]
    score1=0
    score2=0
    paddle1_vel = 0
    paddle2_vel = 0
    paddle1_pos = HEIGHT/2-HALF_PAD_HEIGHT
    paddle2_pos = HEIGHT/2-HALF_PAD_HEIGHT
    spawn_ball(random.random()<0.5)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    #paddle1_pos = HEIGHT/2-HALF_PAD_HEIGHT
    #paddle2_pos = HEIGHT/2-HALF_PAD_HEIGHT
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0]+= ball_vel[0]     
    ball_pos[1]+= ball_vel[1]  
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 0.7, "White", "White")
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos >= HEIGHT-PAD_HEIGHT:
        paddle1_pos =HEIGHT-PAD_HEIGHT
    elif paddle1_pos <= 0:
        paddle1_pos =0
    elif paddle2_pos >= HEIGHT-PAD_HEIGHT:
        paddle2_pos =HEIGHT-PAD_HEIGHT
    elif paddle2_pos <= 0:
        paddle2_pos =0
    paddle1_pos +=paddle1_vel
    paddle2_pos +=paddle2_vel
        
    #canvas.draw_line([0,HEIGHT/2+HALF_PAD_HEIGHT], [0,HEIGHT/2-HALF_PAD_HEIGHT], PAD_WIDTH, "White")
    #canvas.draw_line([WIDTH,HEIGHT/2+HALF_PAD_HEIGHT], [WIDTH,HEIGHT/2-HALF_PAD_HEIGHT], PAD_WIDTH, "White")
    # draw paddles
    canvas.draw_line([0,paddle1_pos], [0,paddle1_pos+PAD_HEIGHT], 2*PAD_WIDTH, "White")
    canvas.draw_line([WIDTH,paddle2_pos], [WIDTH,paddle2_pos+PAD_HEIGHT], 2*PAD_WIDTH, "White")
    
    # determine whether paddle and ball collide
    #if ball_pos[0] <= BALL_RADIUS:
            #ball_vel[0] = - ball_vel[0]
    #elif ball_pos[0] >= WIDTH-BALL_RADIUS:
            #ball_vel[0] = -ball_vel[0]      
    #elif ball_pos[1] <= BALL_RADIUS:
        #ball_vel[1] = -ball_vel[1]
    #elif ball_pos[1] >=HEIGHT-BALL_RADIUS:
        #ball_vel[1] = -ball_vel[1]
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    elif ball_pos[1] >=HEIGHT-BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
        
    if ball_pos[0] <= PAD_WIDTH+BALL_RADIUS:
        if ball_pos[1] <= paddle1_pos+PAD_HEIGHT and ball_pos[1]>=paddle1_pos:
            ball_vel[0] = - 1.1*ball_vel[0]
        else:
            ball_pos = [WIDTH / 2, HEIGHT / 2]
            score2 +=1
            spawn_ball(RIGHT)
            
    if ball_pos[0] >= WIDTH-BALL_RADIUS-PAD_WIDTH:
        if	ball_pos[1] <= paddle2_pos+PAD_HEIGHT and ball_pos[1]>=paddle2_pos:
            ball_vel[0] = - 1.1*ball_vel[0]
        else:
            ball_pos = [WIDTH / 2, HEIGHT / 2]
            score1 +=1
            spawn_ball(LEFT)
            
    # draw scores
    canvas.draw_text("Player A:  "+ str(score1),[20,40],40,"White")
    canvas.draw_text("Player B:  "+ str(score2),[320,40],40,"White")
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    v=3
    if key==simplegui.KEY_MAP["s"]:
        paddle1_vel += v
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel += v
    elif key==simplegui.KEY_MAP["w"]:
        paddle1_vel -= v
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel -= v
    
    
def keyup(key):
    global paddle1_vel, paddle2_vel,current_key
    current_key = ' '
    paddle1_vel=0
    paddle2_vel=0
        
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.add_button("Restart", Restart, 80)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
