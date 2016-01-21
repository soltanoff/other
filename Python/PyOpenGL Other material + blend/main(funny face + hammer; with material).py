#!/usr/bin/python
# -*- coding: utf-8 -*-
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

global cur_light
global light0_on, light1_on, light2_on
global alpha
global beta
global OX, OY, OZ
global speed, movement, t_move

def init_window():
    global cur_light
    global alpha, beta
    global OX, OY, OZ
    global speed, movement, t_move
    global light0_on, light1_on, light2_on

    cur_light = GL_LIGHT0
    movement = speed = 0.02
    t_move = True
    light0_on = light1_on = light2_on = True
    OX = OY = OZ = 0
    alpha =  beta = 0
    glutInit(sys.argv)

    width = 1000
    heigth = 600
    gluPerspective(180.0, float(width)/float(heigth), 0.1, 100.0)
    glutInitWindowSize(width, heigth)
    glutInitWindowPosition(160, 50)
    glutCreateWindow(b"LR2")

    glutInitDisplayMode( GL_RGBA | GL_DEPTH | GL_DOUBLE )

def set_func():
    glutSpecialFunc(keyPressed)
    glutDisplayFunc(display)
    glutKeyboardFunc(classicKeyPressed)
    #glutIdleFunc(IdleFunc)
    glutReshapeFunc(resize)

def light_control(gl_light_, light_on):
    if light_on: glDisable(gl_light_)
    else: glEnable(gl_light_)
    return not light_on

def classicKeyPressed(key, x, y):
    global cur_light
    global OX, OY, OZ
    if key == b'1': cur_light = GL_LIGHT0
    if key == b'2': cur_light = GL_LIGHT1
    if key == b'3': cur_light = GL_LIGHT3
    if key == b'\xe9': OX += 5.5 #Q
    if key == b'\xf4': OX -= 5.5 #A
    if key == b'\xf6': OY += 5.5 #W
    if key == b'\xfb': OY -= 5.5 #S
    if key == b'\xf3': OZ += 5.5 #E
    if key == b'\xe2': OZ -= 5.5 #D
    glutPostRedisplay()

def keyPressed(key, x, y):
    global beta, alpha
    global OX, OY, OZ, movement, t_move
    global light0_on, light1_on, light2_on
    if key == GLUT_KEY_UP: beta += 5.5
    if key == GLUT_KEY_LEFT: alpha -= 5.5
    if key == GLUT_KEY_DOWN: beta -= 5.5
    if key == GLUT_KEY_RIGHT: alpha += 5.5
    if key == GLUT_KEY_F1: light0_on = light_control(GL_LIGHT0, light0_on)
    if key == GLUT_KEY_F2: light1_on = light_control(GL_LIGHT1, light1_on)
    if key == GLUT_KEY_F3: light2_on = light_control(GL_LIGHT3, light2_on)
    if key == GLUT_KEY_F4:
        if t_move: movement = 0.0
        else: movement = speed
        t_move = not t_move
    if key == GLUT_KEY_END: glutIdleFunc(IdleFunc)
    glutPostRedisplay()

def resize(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode( GL_PROJECTION )
    glLoadIdentity()
    glOrtho(-5.0, 5.0, -5.0, 5.0, 2.0, 12.0)
    gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0,0.0)
    glMatrixMode( GL_MODELVIEW )

def IdleFunc():
    global beta
    global alpha
    global movement
    alpha += movement
    beta += movement
    glutPostRedisplay()

def draw_funny_face():
    glPushMatrix()
    #====================== 1 Чайник =================================
    glRotated(180, 0.0, -1.0, 0.0)
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, (1.0, 1.0, 1.0, 1.0))
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, (0.0, 0.0, 0.2, 1.0))
    glMaterialfv(GL_FRONT_AND_BACK, GL_SHININESS, (85.0, 0.0, 0.0))
    glColor3d(1.0, 0.25, 0.8)
    glutSolidTeapot(0.5)
    #====================== 2 Чайник =================================
    glTranslatef(0.8, 0.0, 0.0)
    glRotated(180, 0.0, -1.0, 0.0)
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, (1.0, 1.0, 1.0, 1.0))
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, (0.0, 0.0, 0.2, 1.0))
    glMaterialfv(GL_FRONT_AND_BACK, GL_SHININESS, (60.0, 0.0, 0.0))
    glColor3d(1.0, 0.25, 0.8)
    glutSolidTeapot(0.5)
    #====================== 3 Чайник =================================
    glTranslatef(0.4, 0.0, 0.0)
    glRotated(90, 0.0 , -1.0, 0.0)
    glEnable(GL_BLEND)
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, (1.0, 1.0, 1.0, 1.0))
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, (0.75, 0.75, 0.75, 1.0))
    glMaterialfv(GL_FRONT_AND_BACK, GL_SHININESS, (22.0, 0.0, 0.0))
    glColor4f(1.0, 0.25, 0.8, 0.5)
    glBlendFunc(GL_SRC_ALPHA,GL_ONE)
    glutSolidTeapot(0.8)
    glDisable(GL_BLEND)
    #====================== Сфера =====================================
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, (1.0, 1.0, 1.0, 0.2))
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, (1.0, 1.0, 1.0, 0.2))
    glMaterialfv(GL_FRONT_AND_BACK, GL_SHININESS, (10.0, 1.0, 1.0))
    glColor4d(0.5, 0.25, 0.0, 1.0)
    glutSolidSphere(0.9, 255, 255)

    glPopMatrix()

def draw_hammer():
    #====================================================================
    glRotatef(90, 1.0, 0.0, 0.0)
    glTranslatef(0.0, 0.0, -0.8)
    glPushMatrix()
    #============== Cylinder ============================================
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, (0.0, 1.0, 1.0, 1.0))
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, (1.0, 1.0, 0.0, 0.2))
    glMaterialfv(GL_FRONT_AND_BACK, GL_SHININESS, (85.0, 0.0, 0.0))
    glColor3d(0.2, 0.6, 0.1)
    glutSolidCylinder(0.2, 2.5, 55, 55)
    #=============== Cube ===============================================
    glEnable(GL_BLEND)
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, (1.0, 1.0, 1.0, 1.0))
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, (0.75, 0.75, 0.75, 1.0))
    glMaterialfv(GL_FRONT_AND_BACK, GL_SHININESS, (22.0, 0.0, 0.0))
    glColor4f(0.1, 0.25, 0.8, 0.5)
    glBlendFunc(GL_SRC_ALPHA,GL_ONE)
    glutSolidOctahedron()
    glDisable(GL_BLEND)

    glPopMatrix()

def draw_compose_1():
    glRotated(alpha*2, 0,1,1)

    glPushMatrix()
    glRotated(beta*2, 1,0,0)
    glTranslatef(1.5, 0.0, 0.0)
    draw_funny_face()
    glPopMatrix()
    glPushMatrix()
    glRotated(beta*2, -1,0,0)
    glTranslatef(-1.5, 0.0, 0.0)
    draw_hammer()
    glPopMatrix()

def draw_compose_2():
    glRotated(alpha*2, 0,1,1)
    glRotated(beta*2, 1,0,0)

    glNewList(1, GL_COMPILE)
    #glTranslatef(0.4, 0.0, 0.0)
    glPushMatrix()
    glTranslatef(0.0, 0.5, 0.0)
    glRotatef(0, 1.0, 0.0, 0.0)
    draw_hammer()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(+0.4, -1.5, 0.0)
    #glRotatef(180, 1.0, 0.0, 0.0)
    draw_funny_face()
    glPopMatrix()
    glEndList()

    glCallList(1)

def light_manip():
    global cur_light
    global OX, OY, OZ
    pos = (-1.0, 3.0, 2.0, 0.0)

    glPushMatrix()
    glRotatef(OX, 1.0, 0.0, 1.0)
    glRotatef(OY, 0.0, 1.0, 0.0)
    glRotatef(OZ, 0.0, 0.0, 1.0)

    glLightfv(cur_light, GL_POSITION, pos)
    glPopMatrix()

def display():
    global beta, alpha
    glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )
    glLoadIdentity()
    #light_manip()
    #glRotated(alpha*2, 0,1,0)
    #glRotated(beta*2, 1,0,0)
    #draw_shader()
    #draw_compose_1()
    draw_compose_2()
    #glCallList(1)

    glutSwapBuffers()

def set_light():
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_COLOR_MATERIAL)

    pos = (1.0, 2.0, 2.0, 0.0)
    dir = (-1.0, -1.0, -1.0)
    pos4 = (-1.0, 3.0, 2.0, 1.0)
    dir4 = (-1.0, -1.0, -1.0)
    #amb = (1.0, 1.0, 1.0, 0.5)
    glEnable(GL_LIGHTING)
    '''glEnable(GL_LIGHT4)

    glLightfv(GL_LIGHT4, GL_POSITION, pos4)
    glLightfv(GL_LIGHT4, GL_SPOT_DIRECTION, dir)'''
    #mat_specular = (1.0, 1.0, 1.0, 1.0)

    glEnable(GL_LIGHT0)

    glLightfv(GL_LIGHT0, GL_POSITION, pos)
    glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, dir)

    pos_2 = (6.0, -2.0, 0.0, 1.0)
    col_2 = (1.0, 0.0, 0.0)
    #col_2 = (1.0, 1.0, 1.0)
    glEnable(GL_LIGHT1)
    #glLightfv(GL_LIGHT1, GL_AMBIENT, amb)
    glLightfv(GL_LIGHT1, GL_DIFFUSE, col_2)
    glLightfv(GL_LIGHT1, GL_POSITION, pos_2)
    glLightfv(GL_LIGHT1, GL_SPOT_DIRECTION, dir)

    pos_3 = (-6.0, -3.0, -2.0, 1.0)
    col_3 = (0.0, 1.0, 0.0)
    #col_3 = (1.0, 1.0, 1.0)
    glEnable(GL_LIGHT3)
    #glLightfv(GL_LIGHT3, GL_AMBIENT, amb)
    glLightfv(GL_LIGHT3, GL_DIFFUSE, col_3)
    glLightfv(GL_LIGHT3, GL_POSITION, pos_3)
    glLightfv(GL_LIGHT3, GL_SPOT_DIRECTION, dir)
    #glLightf(GL_LIGHT3, GL_SPOT_CUTOFF, 45)
    #glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    #glMaterialf(GL_FRONT, GL_SHININESS, 128.0)
    pos_4 = (6.0, -2.0, 0.0, 1.0)
    col_4 = (1.0, 1.0, 0.0)
    #col_2 = (1.0, 1.0, 1.0)
    glEnable(GL_LIGHT2)
    #glLightfv(GL_LIGHT1, GL_AMBIENT, amb)
    glLightfv(GL_LIGHT2, GL_DIFFUSE, col_4)
    glLightfv(GL_LIGHT2, GL_POSITION, pos_4)
    glLightfv(GL_LIGHT2, GL_SPOT_DIRECTION, dir)

def view_info():
     print("Контроль:\n",
        "№1 - белый свет, №2 - красный, №3 - зеленый",
        "F1 и F2 и F3 - вкл/выкл источников света №1, №2, №3\n",
        "1, 2, 3, - выбор источнника света №1, №2, №3\n",
        "Ox(Q, A), Oy(W, S), Oz(E, D) - вращение света вручную\n",
        "UP, LEFT, DOWN, RIGHT - вращение сцены вручную\n",
        "F4 - поставить вращение на паузу\n",
        "END - включить вращение сцены\n")

def main():
    init_window()
    set_func()
    set_light()
    view_info()
    #glBlendFunc ( GL_SRC_COLOR, GL_ONE_MINUS_SRC_ALPHA)
    glutMainLoop()
    #gluDeleteNurbsRenderer()

if __name__ == '__main__':
    main()
