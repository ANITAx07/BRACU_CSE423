
# Task 1: Building a House in Rainfall

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

bg_color = (0.0, 0.0, 0.0, 0.0)
speed = 0.5
rain_angle = 0.0
rain_arr = []

def draw_points(x, y): #raindrop
    glColor3f(0.0, 0.0, 1.0)
    glPointSize(3) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x,y) #jekhane show korbe pixel
    glEnd()

def draw_roof():
    glLineWidth(4)
    glBegin(GL_LINES)

    glVertex2f(100, 300)  #left line
    glVertex2f(250, 400)
    glVertex2f(250, 400)  #right line
    glVertex2f(400, 300)
    glVertex2f(100, 300)  #bottom line
    glVertex2f(400, 300)
    glEnd()

def draw_body():
    glLineWidth(4)
    glBegin(GL_LINES)

    glVertex2f(120, 300)  #right line
    glVertex2f(120, 100)

    glVertex2f(380, 300)  #left line
    glVertex2f(380, 100)

    glVertex2f(120, 100)  #middle line
    glVertex2f(380, 100)
    glEnd()

def draw_door():
    glLineWidth(4)
    glBegin(GL_LINES)

    glVertex2f(150, 220) #left line
    glVertex2f(150, 100)

    glVertex2f(220, 220) #right line
    glVertex2f(220, 100)

    glVertex2f(150, 220) #upper line
    glVertex2f(220, 220)

    glEnd()

def draw_window():
    glLineWidth(4)
    glBegin(GL_LINES)

    glVertex2f(265, 200)  # left
    glVertex2f(265, 250)

    glVertex2f(345, 200)  # right
    glVertex2f(345, 250)

    glVertex2f(305, 200) #ver mid
    glVertex2f(305, 250)

    glVertex2f(265, 225) #hor mid
    glVertex2f(345, 225)

    glVertex2f(265, 250)  #upper
    glVertex2f(345, 250)

    glVertex2f(265, 200)  #bottom
    glVertex2f(345, 200)

    glEnd()

def draw_doorknob(x, y):  #same method of draw point
    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def rain_drop():
    global rain_angle
    length = len(rain_arr)
    for i in range(0, length):
        x1, y1 = rain_arr[i]
        x1 += rain_angle
        y1 -= speed
        if 120 < x1 < 380 and 100 < y1 < 300:
            x1 = random.uniform(100, 400)
            y1 = random.uniform(200, 500)
        rain_arr[i] = (x1, y1)

def day_time():
    global bg_color
    bg_color = (1.0, 1.0, 1.0, 1.0)
    print("Day time")

def night_time():
    global bg_color
    bg_color = (0.0, 0.0, 0.0, 0.0)
    print("Night time")

def specialKeyListener(key, a, b):
    global rain_angle

    if key == GLUT_KEY_RIGHT:
        rain_angle += 1
        print('Right')

    if key == GLUT_KEY_LEFT:
        rain_angle -= 1
        print('Left')
    glutPostRedisplay()


def keyboardListener(key, a, b):
    if key == b'd':
        day_time()

    if key == b'n':
        night_time()

    glutPostRedisplay()

def animate():
    rain_drop()
    glutPostRedisplay()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def init():
    #//clear the screen
    glClearColor(0,0,0,0)
    #//load the PROJECTION matrix
    glMatrixMode(GL_PROJECTION)
    #//initialize the matrix
    glLoadIdentity()
    #//give PERSPECTIVE parameters
    gluPerspective(104,	1,	1,	1000.0)
    # **(important)**aspect ratio that determines the field of view in the X direction (horizontally). The bigger this angle is, the more you can see of the world - but at the same time, the objects you can see will become smaller.
    #//near distance
    #//far distance

def showScreen():
    glClearColor(*bg_color)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(0.3, 0.2, 0.1) #konokichur color set (RGB)
    #call the draw methods here
    draw_roof()
    draw_body()
    draw_door()
    draw_window()
    draw_doorknob(210, 175)
    # rain_drop()
    for j in rain_arr:
        draw_points(j[0], j[1])

    glutSwapBuffers()

glutInit()
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB) #	//Depth, Double buffer, RGB color

# glutCreateWindow("My OpenGL Program")
wind = glutCreateWindow(b"OpenGL Coding Practice")
init()

glutDisplayFunc(showScreen)	#display callback function
glutIdleFunc(animate)	#what you want to do in the idle time (when no drawing is occuring)
glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)
# glutMouseFunc(mouseListener)

for j in range(350):
    x_2 = random.uniform(100, 400)
    y_2 = random.uniform(200, 500)
    rain_arr.append((x_2, y_2))

glutMainLoop()






## Task 2: Building the Amazing Box
#
# from OpenGL.GL import *
# from OpenGL.GLUT import *
# from OpenGL.GLU import *
# import random
# W_width = 500
# W_height = 500
#
# random_point = []
# speed = 0.01
# blink = False # blink points
# freeze = False #freeze points
#
# def coordinate(x,y):
#     global W_width, W_height
#     a = x - (W_width/2)
#     b = (W_height/2) - y
#     return a, b
#
# def blink_p(a):
#     global blink
#     if blink is True:
#         blink = False
#         print('Unblink')
#     elif blink is False:
#         blink = True
#         print('blink')
#     glutPostRedisplay()
#
# def keyboardListener(key, a, b):
#     global freeze
#     if key == b' ': #spacebar
#         if freeze is False:
#             freeze = True
#             print('Freezed')
#         elif freeze is True:
#             freeze = False
#             print('unfreezed')
#     glutPostRedisplay()
#
# def specialKeyListener(key, a, b):
#     global speed, freeze
#     if freeze is False:
#         if key == GLUT_KEY_UP:
#             speed *= 5
#             print('speed increased')
#         if key == GLUT_KEY_DOWN:
#             speed /= 5
#             print('speed decreased')
#     glutPostRedisplay()
#
# def mouseListener(button, state, x, y):	#/#/x, y is the x-y of the screen (2D)
#     global random_point, freeze, blink
#     c1 = [-1, 1]
#     c2 = [-1, 1]
#     # color = (random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))
#     if freeze is False:
#         if button == GLUT_RIGHT_BUTTON:
#             if state == GLUT_DOWN:
#                 # random_point.append([(x, y), (random.choice(c1), random.choice(c2)), color])
#                 random_point.append({
#                     'coordinate_pos': coordinate(x, y),
#                     'choice_dir': (random.choice(c1), random.choice(c2)),
#                     'color_choice': (random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))
#                 })
#
#             #print(random_point)
#         elif button == GLUT_LEFT_BUTTON:
#             if state == GLUT_DOWN:
#                 blink = True
#                 print('blinking')
#                 glutTimerFunc(1000, blink_p, 0)
#         glutPostRedisplay()
#
# def animate():
#     glutPostRedisplay()
#     global W_width, W_height, random_point, speed, freeze
#
#     if freeze is False:
#         for i in random_point:
#             x1, y1 = i['coordinate_pos']
#             x2, y2 = i['choice_dir']
#             x1 = x1 + (x2 * speed)
#             y1 = y1 + (y2 * speed)
#             if x1 < 0 or x1 > W_width:
#                 i['choice_dir'] = (-x2, y2)
#             if y1 < 0 or y1 > W_height:
#                 i['choice_dir'] = (x2, -y2)
#             i['coordinate_pos'] = (x1, y1)
#
# def iterate():
#     glViewport(0, 0, 500, 500)
#     glMatrixMode(GL_PROJECTION)
#     glLoadIdentity()
#     glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
#     glMatrixMode(GL_MODELVIEW)
#     glLoadIdentity()
#
# # def init():
# #     #//clear the screen
# #     glClearColor(0,0,0,0)
# #     #//load the PROJECTION matrix
# #     glMatrixMode(GL_PROJECTION)
# #     #//initialize the matrix
# #     glLoadIdentity()
# #     #//give PERSPECTIVE parameters
# #     gluPerspective(104,	1,	1,	1000.0)
# #     # **(important)**aspect ratio that determines the field of view in the X direction (horizontally). The bigger this angle is, the more you can see of the world - but at the same time, the objects you can see will become smaller.
# #     #//near distance
# #     #//far distance
#
# def showScreen():
#     global speed, blink, random_point
#     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#     glLoadIdentity()
#     iterate()
#     glColor3f(0.0, 0.0, 0.0)
#     if len(random_point) > 0:
#         for i in random_point:
#             a, b = i['coordinate_pos']
#             glPointSize(10)
#             glBegin(GL_POINTS)
#             if blink is False:
#                 glColor3f(0.0, 0.0, 0.0)
#             else:
#                 glColor3f(i['color_choice'][0], i['color_choice'][1], i['color_choice'][2])
#             glVertex2f(a, b)
#             glEnd()
#     glutSwapBuffers()
#
#
# glutInit()
# glutInitWindowSize(W_width, W_height)
# glutInitWindowPosition(0, 0)
# glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB) #	//Depth, Double buffer, RGB color
#
# # glutCreateWindow("My OpenGL Program")
# wind = glutCreateWindow(b"OpenGL Coding Practice")
# # init()
#
# glutDisplayFunc(showScreen)	#display callback function
# glutIdleFunc(animate)	#what you want to do in the idle time (when no drawing is occuring)
#
# glutKeyboardFunc(keyboardListener)
# glutSpecialFunc(specialKeyListener)
# glutMouseFunc(mouseListener)
#
# glutMainLoop()
