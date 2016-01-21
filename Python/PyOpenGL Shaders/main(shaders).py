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

def create_shader(shader_type, source):
    # Создаем пустой объект шейдера
    shader = glCreateShader(shader_type)
    # Привязываем текст шейдера к пустому объекту шейдера
    glShaderSource(shader, source)
    # Компилируем шейдер
    glCompileShader(shader)
    # Возвращаем созданный шейдер
    return shader

def test():
    #pointdata = [[1.0, 1.0,-1.0], [-1.0, 1.0,-1.0], [-1.0, 1.0, 1.0], [1.0, 1.0, 1.0],
      #  [1.0,-1.0, 1.0], [-1.0,-1.0, 1.0], [-1.0,-1.0,-1.0], [1.0,-1.0,-1.0],
      #  [1.0, 1.0, 1.0], [-1.0, 1.0, 1.0], [-1.0,-1.0, 1.0], [1.0,-1.0, 1.0],
      #  [1.0,-1.0,-1.0], [-1.0,-1.0,-1.0], [-1.0, 1.0,-1.0], [1.0, 1.0,-1.0],
      #  [-1.0, 1.0, 1.0], [-1.0, 1.0,-1.0], [-1.0,-1.0,-1.0], [-1.0,-1.0, 1.0],
      #  [1.0, 1.0,-1.0], [1.0, 1.0, 1.0], [1.0,-1.0, 1.0], [1.0,-1.0,-1.0]]
    pointdata2 = [
      [1.0, -1.0, -1.0],
      [1.0, 1.0, -1.0],
      [-1.0,  1.0, -1.0],
      [-1.0, -1.0, -1.0],
      [1.0, -1.0,  1.0],
      [1.0, 1.0,  1.0],
      [-1.0,  -1.0,  -1.0],
      [-1.0,  1.0,  1.0]
    ]
    #index = [
     #   0, 3, 1,  1, 3, 2, # front
      #  4, 7, 5,  5, 7, 6, # back
     #   8,11, 9,  9,11,10, # top
       # 12,15,13, 13,15,14, # bottom
       # 16,19,17, 17,19,18, # left
       # 20,23,21, 21,23,22  # right
    #]
    pointdata1 = [
        [-1.0,-1.0,-1.0], [-1.0,-1.0, 1.0], [-1.0, 1.0, 1.0],   #1 треугольник
        [1.0, 1.0,-1.0], [-1.0,-1.0,-1.0], [-1.0, 1.0,-1.0],    #2 треугольник
        [1.0,-1.0, 1.0], [-1.0,-1.0,-1.0], [1.0,-1.0,-1.0],     #3 треугольник
        [1.0, 1.0,-1.0], [1.0,-1.0,-1.0], [-1.0,-1.0,-1.0],     #4 треугольник
        [-1.0,-1.0,-1.0], [-1.0, 1.0, 1.0], [-1.0, 1.0,-1.0],   #5 треугольник
        [1.0,-1.0, 1.0], [-1.0,-1.0, 1.0], [-1.0,-1.0,-1.0],    #6 треугольник
        [-1.0, 1.0, 1.0], [-1.0,-1.0, 1.0], [1.0,-1.0, 1.0],    #7 треугольник
        [1.0, 1.0, 1.0], [1.0,-1.0,-1.0], [1.0, 1.0,-1.0],      #8 треугольник
        [1.0,-1.0,-1.0], [1.0, 1.0, 1.0], [1.0,-1.0, 1.0],      #9 треугольник
        [1.0, 1.0, 1.0], [1.0, 1.0,-1.0], [-1.0, 1.0,-1.0],     #10 треугольник
        [1.0, 1.0, 1.0], [-1.0, 1.0,-1.0], [-1.0, 1.0, 1.0],    #11 треугольник
        [1.0, 1.0, 1.0], [-1.0, 1.0, 1.0], [1.0,-1.0, 1.0]      #12 треугольник
    ]
    pointcolor = [
        [1, 1, 0], [0, 1, 1], [1, 0, 1],      #1 треугольник
        [1, 0, 0], [0, 1, 0], [0, 0, 1],      #2 треугольник
        [0, 0, 0], [0, 0, 0], [0, 0, 1],      #3 треугольник
        [1, 0, 0], [0, 0, 1], [0, 1, 0],      #4 треугольник
        [1, 1, 0], [1, 0, 1], [1, 1, 1],      #5 треугольник
        [0, 0, 0], [0, 0, 1], [0, 0, 0],      #6 треугольник
        [0, 1, 1], [1, 0, 1], [1, 1, 1],      #7 треугольник
        [0.8, 0.2, 0.2], [0.5, 1, 0], [0.2, 0.4, 0.75],      #8 треугольник
        [0.5, 1, 0], [0.8, 0.2, 0.2], [0.2, 0.4, 0.75],      #9 треугольник
        [1, 1, 0], [1, 1, 1], [1, 1, 0],      #10 треугольник
        [1, 1, 0], [1, 1, 0], [1, 1, 1],      #11 треугольник
        [1, 0, 1], [0, 1, 1], [1, 1, 1]       #12 треугольник
    ]
    glDrawArrays(GL_TRIANGLES, 0, 36)

def draw_shader():
    # Положение вершин не меняется
    # Цвет вершины - такой же как и в массиве цветов

    vertex = create_shader(GL_VERTEX_SHADER, """
    varying vec4 vertex_color;
        void main(){
            gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
            vertex_color = gl_Color;
        }""")
    fragment = create_shader(GL_FRAGMENT_SHADER, """
    varying vec4 vertex_color;
        void main() {
            gl_FragColor = vertex_color;
        }""")

    program = glCreateProgram()
    glAttachShader(program, vertex)
    glAttachShader(program, fragment)
    glLinkProgram(program)
    glUseProgram(program)

    #pointdata = [[0, 1.5, 0], [-1.5, -1.5, 0], [1.5, -1.5, 0]]#, [1.5, 0, 0]]
    #pointcolor = [[1, 1, 0], [0, 1, 1], [1, 0, 1]]
    pointdata = [
        [-1.0,-1.0,-1.0], [-1.0,-1.0, 1.0], [-1.0, 1.0, 1.0],   #1 треугольник
        [1.0, 1.0,-1.0], [-1.0,-1.0,-1.0], [-1.0, 1.0,-1.0],    #2 треугольник
        [1.0,-1.0, 1.0], [-1.0,-1.0,-1.0], [1.0,-1.0,-1.0],     #3 треугольник
        [1.0, 1.0,-1.0], [1.0,-1.0,-1.0], [-1.0,-1.0,-1.0],     #4 треугольник
        [-1.0,-1.0,-1.0], [-1.0, 1.0, 1.0], [-1.0, 1.0,-1.0],   #5 треугольник
        [1.0,-1.0, 1.0], [-1.0,-1.0, 1.0], [-1.0,-1.0,-1.0],    #6 треугольник
        [-1.0, 1.0, 1.0], [-1.0,-1.0, 1.0], [1.0,-1.0, 1.0],    #7 треугольник
        [1.0, 1.0, 1.0], [1.0,-1.0,-1.0], [1.0, 1.0,-1.0],      #8 треугольник
        [1.0,-1.0,-1.0], [1.0, 1.0, 1.0], [1.0,-1.0, 1.0],      #9 треугольник
        [1.0, 1.0, 1.0], [1.0, 1.0,-1.0], [-1.0, 1.0,-1.0],     #10 треугольник
        [1.0, 1.0, 1.0], [-1.0, 1.0,-1.0], [-1.0, 1.0, 1.0],    #11 треугольник
        [1.0, 1.0, 1.0], [-1.0, 1.0, 1.0], [1.0,-1.0, 1.0]      #12 треугольник
    ]
    pointcolor = [
        [1, 1, 0], [0, 1, 1], [1, 0, 1],      #1 треугольник
        [1, 0, 0], [0, 1, 0], [0, 0, 1],      #2 треугольник
        [0, 0, 0], [0, 0, 0], [0, 0, 1],      #3 треугольник
        [1, 0, 0], [0, 0, 1], [0, 1, 0],      #4 треугольник
        [1, 1, 0], [1, 0, 1], [1, 1, 1],      #5 треугольник
        [0, 0, 0], [0, 0, 1], [0, 0, 0],      #6 треугольник
        [0, 1, 1], [1, 0, 1], [1, 1, 1],      #7 треугольник
        [0.8, 0.2, 0.2], [0.5, 1, 0], [0.2, 0.4, 0.75],      #8 треугольник
        [0.5, 1, 0], [0.8, 0.2, 0.2], [0.2, 0.4, 0.75],      #9 треугольник
        [1, 1, 0], [1, 1, 1], [1, 1, 0],      #10 треугольник
        [1, 1, 0], [1, 1, 0], [1, 1, 1],      #11 треугольник
        [1, 0, 1], [0, 1, 1], [1, 1, 1]       #12 треугольник
    ]



    glClear(GL_COLOR_BUFFER_BIT)                    # Очищаем экран и заливаем серым цветом
    glEnableClientState(GL_VERTEX_ARRAY)            # Включаем использование массива вершин
    glEnableClientState(GL_COLOR_ARRAY)             # Включаем использование массива цветов
    # Указываем, где взять массив верши:
    glVertexPointer(3, GL_FLOAT, 0, pointdata)
    # Указываем, где взять массив цветов:
    glColorPointer(3, GL_FLOAT, 0, pointcolor)
    # Рисуем данные массивов за один проход:
    glDrawArrays(GL_TRIANGLES, 0, 36)
    glDisableClientState(GL_VERTEX_ARRAY)           # Отключаем использование массива вершин
    glDisableClientState(GL_COLOR_ARRAY)            # Отключаем использование массива цветов
    #glDrawElements(GL_TRIANGLES, index, GL_UNSIGNED_INT, 0)

def display():
    global beta, alpha
    glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )
    glLoadIdentity()
    #light_manip()
    #glRotated(alpha*2, 0,1,0)
    #glRotated(beta*2, 1,0,0)
    draw_shader()

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
