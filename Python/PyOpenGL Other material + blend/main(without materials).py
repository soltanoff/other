#!/usr/bin/python
# -*- coding: utf-8 -*-
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

global alpha
global beta

def init_window():
    global alpha, beta
    alpha =  beta = 0
    glutInit(sys.argv)

    width = 1000
    heigth = 600
    gluPerspective(180.0, float(width)/float(heigth), 0.1, 100.0)
    glutInitWindowSize(width, heigth)
    glutInitWindowPosition(160, 50)
    glutCreateWindow(b"LR2")

    glutInitDisplayMode( GL_RGB | GL_DEPTH | GL_DOUBLE )

def set_func():
    glutSpecialFunc(keyPressed)
    glutDisplayFunc(display)
    glutIdleFunc(IdleFunc)
    glutReshapeFunc(resize)

def keyPressed(key, x, y):
    global beta, alpha
    if key == GLUT_KEY_UP: beta += 5.5
    if key == GLUT_KEY_LEFT: alpha -= 5.5
    if key == GLUT_KEY_DOWN: beta -= 5.5
    if key == GLUT_KEY_RIGHT: alpha += 5.5
    glutPostRedisplay()  # вызов ерерисовки

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
    alpha += 0.2
    beta += 0.2
    glutPostRedisplay()

def draw_teapot():
    glPushMatrix()
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, (1.0, 1.0, 1.0, 1.0))
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, (1.0, 1.0, 1.0, 1.0))
    glMaterialfv(GL_FRONT_AND_BACK, GL_SHININESS, (128.0, 1.0, 1.0))
    glColor3d(0.25, 0.25, 0.8)
    glutSolidTeapot(1.0)

    glPopMatrix();

def draw_cube():
    glPushMatrix()
    #glLoadIdentity()
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, (1.0, 0.0, 1.0, 0.0))
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, (1.0, 1.0, 1.0, 1.0))
    glMaterialfv(GL_FRONT_AND_BACK, GL_SHININESS, (25.0, 1.0, 1.0))
    glColor3d(0.2, 0.2, 0.2)
    #glutSolidCube(1.5)
    glutSolidDodecahedron()
    glPopMatrix()

def draw_compose():
    glTranslatef(0.0, 0.0, -3.0)
    #Вращаем плоскость
    glRotated(alpha, 0.0, 1.0, 1.0)
    glTranslatef(0.0, 2.0, 0.0)
    #==============1 чайник==============
    glPushMatrix();
    glTranslatef(2.0, 0.0, 0.0)
    glRotated(-alpha*2, 0,1,1);
    glRotated(beta*2, 1,0,0)
    draw_teapot()
    glPopMatrix();
    #==============2 чайник==============
    glPushMatrix();
    glTranslatef(-2.0, 0.0, 0.0)
    glRotated(alpha*2, 0,1,0);
    glRotated(-beta*5, 1,0,1)
    draw_teapot()
    glPopMatrix();
    #================Кубик===============
    glPushMatrix();
    glTranslatef(0.0, -2.0, 0.0)
    glRotated(-alpha, 1,1,0);
    #glRotated(-beta, 1,0,0)
    #draw_teapot()
    draw_cube()
    glPopMatrix();
    #==============3 чайник==============
    glTranslatef(0.0, -4.0, 0.0)
    glPushMatrix();
    glTranslatef(2.0, 0.0, 0.0)
    glRotated(alpha*6, 0,1,1);
    #glRotated(-beta, 1,0,0)
    draw_teapot()
    glPopMatrix();
    #==============4 чайник==============
    glPushMatrix();
    glTranslatef(-2.0, 0.0, 0.0)
    glRotated(-alpha*3, 1,1,0);
    glRotated(beta*2, 0,0,1)
    draw_teapot()
    glPopMatrix();

def display():
    global beta, alpha
    glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT );
    #glLoadIdentity()
    #glutSolidCube(2.0)
    draw_compose()
    glutSwapBuffers();

def set_light():
    glEnable(GL_DEPTH_TEST);
    glEnable(GL_COLOR_MATERIAL);

    pos = (-1.0, 3.0, 2.0, 0.0)
    dir = (-1.0, -1.0, -1.0);

    mat_specular = (1.0, 1.0, 1.0, 1.0);
    glEnable(GL_LIGHTING);
    glEnable(GL_LIGHT0);

    glLightfv(GL_LIGHT0, GL_POSITION, pos);
    glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, dir);

    pos_2 = (1.0, -1.0, 2.0, 1.0)
    col_2 = (1.0, 0.0, 0.0, 1.0)
    glEnable(GL_LIGHT1)
    glLightfv(GL_LIGHT1, GL_DIFFUSE, col_2);
    glLightfv(GL_LIGHT1, GL_POSITION, pos_2);
    glLightfv(GL_LIGHT1, GL_SPOT_DIRECTION, dir);

    pos_3 = (-6.0, -3.0, -2.0, 1.0)
    col_3 = (0.0, 1.0, 0.0)
    glEnable(GL_LIGHT3)
    glLightfv(GL_LIGHT3, GL_DIFFUSE, col_3);
    glLightfv(GL_LIGHT3, GL_POSITION, pos_3);
    glLightfv(GL_LIGHT3, GL_SPOT_DIRECTION, dir);
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular);
    glMaterialf(GL_FRONT, GL_SHININESS, 128.0);

def main():

    global alpha, beta
    alpha =  beta = 0
    glutInit(sys.argv)

    width = 1000
    heigth = 600
    gluPerspective(180.0, float(width)/float(heigth), 0.1, 100.0)
    glutInitWindowSize(width, heigth)
    glutInitWindowPosition(160, 50)
    glutCreateWindow(b"LR2")

    glutInitDisplayMode( GL_RGB | GL_DEPTH | GL_DOUBLE )


    glutSpecialFunc(keyPressed)
    glutDisplayFunc(display)
    glutIdleFunc(IdleFunc)
    glutReshapeFunc(resize)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_COLOR_MATERIAL)


    #glutKeyboardFunc(numberPress)
    #glScalef(0.5, 0.5, 0.5)
    glutMainLoop()

if __name__ == '__main__':
    main()
