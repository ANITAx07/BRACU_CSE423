from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

#screen
W_width, W_height = 800, 800
game_state = 'playing'
quit_flag = False
timer_flag = False

#colors
black_background = (0.0, 0.0, 0.0)
white = (1.0, 1.0, 1.0)
red = (1.0, 0.0, 0.0)
green = (0.0, 1.0, 0.0)
blue = (0.0, 0.0, 1.0)
yellow = (1.0, 1.0, 0.0)
amber = (1.0, 0.75, 0.0)

#button
button_width, button_height = 150, 200

#circle
falling_circle_lst = []
projectile_lst = []
center_x, center_y = W_width//2, W_height//2
radius = 20
score = 0
misses = 0
missed_shots = 0

#shooter
shooter_position = W_width // 2

def projectile():
    for x, y, radius in projectile_lst:
        draw_circle(x, y, radius)  #to show circle or projectile on the screen

for i in range(5):  #5 circle at a time
    x_min = 30   #ekdom left theke jno start na hoy
    x_max = W_width - 30    # ekdom right
    y_min = 600
    y_max = 700
    min_radius = 15
    max_radius = 25
    x = random.randint(x_min, x_max)
    y = random.randint(y_min, y_max)
    radius = random.randint(min_radius, max_radius)
    falling_circle_lst.append([x, y, radius])    #new generated circle

def draw_circle(center_x,center_y,radius):
    x = 0
    y = radius
    d = 1 - radius
    glPointSize(3)

    glColor3f(*yellow)
    glBegin(GL_POINTS)

    circle_points(center_x, center_y, x, y)
    while x < y:
        x += 1
        if d < 0:
            d += 2 * x + 3
        else:
             y -= 1
             d += 2*x - 2*y + 5
        circle_points(center_x, center_y, x, y)
    glEnd()

def circle_points(center_x, center_y, x, y):
    for i in range(8):
        new_x, new_y = eightway_to_other(x, y, i)
        glVertex2f(center_x + new_x, center_y + new_y)

def eightway_to_zero(x1, y1, x2, y2, zone):
        if zone == 1:
            return y1, x1, y2, x2
        elif zone == 2:
            return y1, -x1, y2, -x2
        elif zone == 3:
            return -x1, y1, -x2, y2
        elif zone == 4:
            return -x1, -y1, -x2, -y2
        elif zone == 5:
            return -y1, -x1, -y2, -x2
        elif zone == 6:
            return -y1, x1, -y2, x2
        elif zone == 7:
            return x1, -y1, x2, -y2
        return x1, y1, x2, y2

def eightway_to_other(x, y, zone):
        if zone == 0:
            return x, y
        elif zone == 1:
            return y, x
        elif zone == 2:
            return -y, x
        elif zone == 3:
            return -x, y
        elif zone == 4:
            return -x, -y
        elif zone == 5:
            return -y, -x
        elif zone == 6:
            return y, -x
        elif zone == 7:
            return x, -y

def find_zone(x1, y1, x2, y2):
    dy = y2 - y1
    dx = x2 - x1
    if abs(dy) > abs(dx):
        if dy >= 0 and dx >= 0:
            return 1
        elif dy >= 0 and dx <= 0:
            return 2
        elif dy <= 0 and dx <= 0:
            return 5
        elif dy <= 0 and dx >= 0:
            return 6
    else:
        if dy >= 0 and dx >= 0:
            return 0
        elif dy >= 0 and dx <= 0:
            return 3
        elif dy <= 0 and dx <= 0:
            return 4
        elif dy <= 0 and dx >= 0:
            return 7

def midpoint_line_algorithm(x1, y1, x2, y2):
    zone = find_zone(x1, y1, x2, y2)
    x_1, y_1, x_2, y_2 = eightway_to_zero(x1, y1, x2, y2, zone)
    dx = x_2 - x_1
    dy = y_2 - y_1
    d = 2 * dy - dx
    dNE = 2 * dy
    dE = (2 * dy) - (2 * dx)
    x = x_1
    y = y_1
    glPointSize(5)
    glBegin(GL_POINTS)
    while x <= x_2:
        a, b = eightway_to_other(x, y, zone)
        glVertex2f(a, b)
        if d < 0:
            x += 1
            d += dE
        else:
            x+=1
            y += 1
            d += dNE
    glEnd()

def falling_circle():
    global falling_circle_lst
    for i in falling_circle_lst:
        x, y, radius = i
        new_x = x
        new_y = y
        draw_circle(new_x, new_y, radius)

def draw_buttons():
    #quit button on right
    draw_cross_button(W_width - 50, W_height - 50)

    #pause or play button on middle
    draw_play_or_pause(W_width // 2, W_height - 50, 50)

    #arrow on left
    draw_arrow(50, W_height - 50, 'left')

def draw_cross_button(x, y):
    glColor3f(*red)
    midpoint_line_algorithm(x - 20, y - 20, x + 20, y + 20)
    midpoint_line_algorithm(x - 20, y + 20, x + 20, y - 20)

def draw_play_or_pause(x, y, size):
    glColor3f(*amber)
    if game_state == 'playing':
        # Two vertical lines
        midpoint_line_algorithm(x - 20, y + 20, x - 20, y - 20)
        midpoint_line_algorithm(x + 20, y + 20, x + 20, y - 20)

    else:
        glColor3f(*green)  # red
        midpoint_line_algorithm(x - 20, y + 10, x + 20, y)
        midpoint_line_algorithm(x - 20, y - 10, x + 20, y)

def draw_arrow(x, y, direction):
    global score
    glColor3f(*blue)
    if direction == 'left':
        midpoint_line_algorithm(x, y, x - 20, y)
        midpoint_line_algorithm(x - 10, y + 5, x - 20, y)
        midpoint_line_algorithm(x - 10, y - 5, x - 20, y)

def shooter():
    glBegin(GL_POINTS)
    # rocket body
    glColor3f(*white)
    for i in range(-8, 9):
        for j in range(10, 50):
            glVertex2i(shooter_position + i, j)

    #rocket's upper triangle
    glColor3f(*red)
    for i in range(-10, 11):
        for j in range(50, 70 - abs(i) * 2):
            glVertex2i(shooter_position + i, j)

    # rocket fin
    for i in range(-20, -7):
        for j in range(10, 10 + (i + 20)):
            glVertex2i(shooter_position + i, j)
    for i in range(8, 21):
        for j in range(10, 10 + (20 - i)):
            glVertex2i(shooter_position + i, j)

    #rocket bottom part
    for i in range(-6, -1):
        for j in range(0, 10):
            glVertex2i(shooter_position + i, j)
    for i in range(0, 5):
        for j in range(0, 10):
            glVertex2i(shooter_position + i, j)
    for i in range(6, 11):
        for j in range(0, 10):
            glVertex2i(shooter_position + i, j)
    glEnd()

def play_pause():
    global game_state
    # glColor3f(*green)
    if game_state == 'paused':
        game_state = 'playing'
    else:
        game_state = 'paused'
    print(f"Game {game_state}")

def button_click(x, y):
    if 50 <= x <= 100 and W_height - 60 <= y <= W_height:
        reset_game()
    elif W_width // 2 - 25 <= x <= W_width // 2 + 25 and W_height - 60 <= y <= W_height:
        play_pause()
    elif W_width - 100 <= x <= W_width - 50 and W_height - 60 <= y <= W_height:
        print('Game Closed')
        glutLeaveMainLoop() #quit

def reset_game():
    global game_state ,score
    print('Game Restarted')
    score = 0  #restart dile ja score chilo jta back to zero
    game_state = 'paused'

def mouseListener(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        button_click(x, W_height - y)

def keyboardListener(key, a, b):
    global quit_flag, shooter_position
    size = 10
    if key == b'x':
        quit_flag = True
    elif key == b'a':
        shooter_position -= size
        if shooter_position - radius < 0:  #cicle off screen to left
            shooter_position = radius
    elif key == b'd':
        shooter_position += size
        if shooter_position + radius > W_width:  #cicle off screen to right
            shooter_position = W_width - radius
    elif key == b' ':
        projectile_lst.append((shooter_position, 50, 20))

def update(value):
    #value for timer callback function
    global falling_circle_lst, projectile_lst, W_height, game_state, score, missed_shots, misses, timer_flag

    if game_state == 'playing':
        new_projectile_lst = []
        for x, y, radius in projectile_lst:
            projectile_collided_flag = False
            for i in range(len(falling_circle_lst)):
                x1, y1, r1 = falling_circle_lst[i]
                if check_collision(x1, y1, r1, x, y, radius):  # circle shoot korle score + hoy new circle generate hoy
                    score += 1
                    falling_circle_lst.pop(i)
                    new_x = random.randint(30, W_width - 30)
                    new_y = random.randint(600, 700)
                    new_radius = random.randint(15, 25)
                    falling_circle_lst.append([new_x, new_y, new_radius])
                    projectile_collided_flag = True

            # projectile er new position screen height er baire jacche kina
            if not projectile_collided_flag: #shoot na korle flag false tai y + hocche
                new_y = y + 20 #can adjust to new value
                if new_y < W_height:  #within screen
                    new_projectile_lst.append((x, new_y, radius))
                else:
                    missed_shots += 1  #shoot  kore pura height jodi cover kore
        #remaining projectile diye update hocche
        projectile_lst = new_projectile_lst

         # checking screen er baire jokhn chole jacche
        for i in range(len(falling_circle_lst)):
            x, y, radius = falling_circle_lst[i]
            y -= 1.0                         #falling circle er y komche
            if y + radius < 0:               # falling circle screen er baire gele new generate hocche top e
                x = random.randint(radius, W_width - radius)
                y = random.randint(600, 700)
                misses += 1
            falling_circle_lst[i] = [x, y, radius]

            if check_collision(x, y, radius, shooter_position, 50, 20):
                game_state = 'Game Over'
                print('Game Over: Hit by a falling circles.')
                print(f"Score: {score}")
                break

            if misses >= 3:
                game_state = 'Game Over'
                print('Game Over: Missed 3 falling circles.')
                print(f"Score: {score}")
                break

            if missed_shots >= 3:
                game_state = 'Game Over'
                print('Game Over: Missed 3 shots.')
                print(f"Score: {score}")
                break

    if game_state != 'Game Over':
        glutPostRedisplay()  #state update kore
        glutTimerFunc(30, update, 10)  #(time ms, callback, value(lage nai))
    else:
        timer_flag = False
    # 30 ms por update function executed hocche
    #value for trigger
    #

def check_collision(x1, y1, r1, x2, y2, r2):   #from assignment doc
    box1 = {'x': x1 - r1, 'y': y1 - r1, 'width': r1 * 2, 'height': r1 * 2}
    box2 = {'x': x2 - r2, 'y': y2 - r2, 'width': r2 * 2, 'height': r2 * 2}

    return (box1['x'] < box2['x'] + box2['width'] and
            box1['x'] + box1['width'] > box2['x'] and
            box1['y'] < box2['y'] + box2['height'] and
            box1['y'] + box1['height'] > box2['y'])

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(0, W_width, 0, W_height)   #clipping window er jonno
#     (left, right, bottom, top)
#     left = 0
#     right = screen width = 800
#     bottom = 0
#     top =  screen height = 800

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_buttons()
    shooter()
    falling_circle()
    projectile()
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(W_width, W_height)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice")
init()  # Set up initial OpenGL environment
glutDisplayFunc(showScreen)  # Register display callback
glutMouseFunc(mouseListener)  # Register mouse click callback
glutKeyboardFunc(keyboardListener)  # Register keyboard for special keys
glutTimerFunc(30, update, 0)  # Initialize timer callback to start
glutMainLoop()