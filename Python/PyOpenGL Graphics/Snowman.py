#!/usr/bin/python
# -*- coding: utf-8 -*-
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

global alpha, beta



def draw_init():
    global alpha, beta
    alpha = beta = 0
    glutInit(sys.argv)

    pos = (3.0, 3.0, 3.0, 1.0)
    dir = (-1.0, -1.0, -1.0)
    mat_specular = (1.0, 1.0, 1.0, 1.0)

    #glutPositionWindow( 50, 10, 400, 400)
    glutInitDisplayMode( GLUT_RGBA | GLUT_DEPTH | GLUT_DOUBLE )
    glutCreateWindow( b"Controls" )
    #glutIdleFunc(display)
    glEnable(GL_DEPTH_TEST)

    glEnable(GL_COLOR_MATERIAL)

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

    glLightfv(GL_LIGHT0, GL_POSITION, pos)
    glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, dir)

    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialf(GL_FRONT, GL_SHININESS, 128.0)
	
	
	
def set_func():
    glutReshapeFunc(resize)
    glutDisplayFunc(display)
    glutKeyboardFunc(key_pressed)
	
	
	
def resize(width, height):
    glViewport(0,0,width,height)
    glMatrixMode( GL_PROJECTION )
    glLoadIdentity()
    glOrtho(-5,5, -5,5, 2,12)
    gluLookAt(0, 0, 5, 0,0,0, 0,1,0 )
    glMatrixMode( GL_MODELVIEW )

	
	
def key_pressed(key):
    if key == GLUT_KEY_UP: alpha += 5
    if key == GLUT_KEY_DOWN: alpha -= 5
    glutPostRedisplay(display)

	
	
def snowman():
    glPushMatrix()

    glColor3d(0.75,0.75,0.75)

    glTranslated(0,-3,0)
    glutSolidSphere(2.0)

    glTranslated(0,3,0)
    glutSolidSphere(1.5)

    glTranslated(0,2,0)
    glutSolidSphere(1)

    glColor3d(0,0,0)

    glTranslated(-0.3,0.3,1)
    glutSolidSphere()

    glTranslated(0.6,0,0)
    glutSolidSphere(0.1)

    glTranslated(-0.3,-0.3,0)
    glColor3d(1,0,0)
    glutSolidCone(0.3,0.5)

    glTranslated(0,0.75,-1)
    glColor3d(0,0,1)
    glRotated(-90,1,0,0)
    glutSolidCone(0.75,0.75)
    glPopMatrix()

	

def display():
    global alpha, beta
    glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT );
    glPushMatrix()
    glRotated(alpha, 0,1,0)
    glRotated(beta, -1,0,0)
    #glutSolidTorus(0.5, 1)
    snowman()
    glPopMatrix()

    glutSwapBuffers()

	
	
	
def main():
    draw_init()
    set_func()
    glutMainLoop()

	
	
if __name__ == '__main__':
	main()
