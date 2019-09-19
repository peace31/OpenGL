import pygame
from pygame.locals import  *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random
radius=0.7
L=10
sclip=50
verticies =(
    (L,-L,-L),
    (L,L,-L),
    (-L,L,-L),
    (-L,-L,-L),
    (L,-L,L),
    (L,L,L),
    (-L,-L,L),
    (-L,L,L)
)
edges=(
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
)
def Cube():
    glBegin(GL_LINES)

    for edge in edges:
        for vertex in edge:
            glColor3fv((0,0.5,0.8))
            glVertex3fv(verticies[vertex])
    glEnd()
def points(number):
    px=[]
    py=[]
    pz=[]
    for i in range(number):
        x=random.uniform(-L+radius,L-radius)
        y = random.uniform(-L + radius, L - radius)
        z = random.uniform(-L + radius, L - radius)
        px.append(x)
        py.append(y)
        pz.append(z)
    return px,py,pz
def update_position(value):
    increment = 1
    nn=random.randint(-1,1)
    value+=nn*increment
    if (value < -L + radius):
        value = -L + radius
    if (value > L - radius):
        value = L - radius
    return value
def random_Spheres(number):
    for i in range(number):
        glPushMatrix()
        glMaterialfv(GL_FRONT, GL_DIFFUSE, (1, 0, 0))
        quadratic = gluNewQuadric()
        ppx[i]=update_position(ppx[i])
        ppy[i] = update_position(ppy[i])
        ppz[i] = update_position(ppz[i])
        glTranslatef(ppx[i], ppy[i], ppz[i])
        glRotatef(20, 30, -20, 0)
        glColor3fv((0.2, 0.8, 0.2))
        gluSphere(quadratic, radius, sclip, sclip)
        glPopMatrix()
def main():
    global px, py, pz, increment
    global ppx,ppy,ppz
    number=10
    ppx,ppy,ppz=points(number)
    px = 0.0
    py = 0.0
    pz = 0.0
    increment = 0.1
    pygame.init()
    display=(500,500)
    pygame.display.set_caption('OpenGL Window')
    pygame.display.set_mode(display,DOUBLEBUF|OPENGL)
    gluPerspective(1,(0.8),0.1,2500.0)
    glTranslatef(0.0, 0, -2400)
    glRotatef(20, 30, -20, 0)


    while True:
        # stop event
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        # key pressed event
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            px+=increment
            if(px>L-radius):
                px=L-radius
        elif keys[K_RIGHT]:
            px-=increment
            if (px < -L+radius):
                px = -L+radius
        elif keys[K_UP]:
            pz+=increment
            if (pz > L-radius):
                pz = L-radius
        elif keys[K_DOWN]:
            pz-=increment
            if (pz < -L+radius):
                pz = -L+radius
        elif keys[K_n]:
            py+=increment
            if (py > L-radius):
                py = L-radius
        elif keys[K_m]:
            py-=increment
            if (py < -L+radius):
                py = -L+radius
        # create cube
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        # create main Sphere
        glPushMatrix()
        glMaterialfv(GL_FRONT, GL_DIFFUSE, (1, 0, 0))
        quadratic = gluNewQuadric()
        glTranslatef(px,py,pz)
        glRotatef(20, 30, -20, 0)
        glColor3fv((1, 0.5, 0.8))
        gluSphere(quadratic,radius,sclip,sclip)
        glPopMatrix()
        random_Spheres(number)
        pygame.display.flip()
        pygame.time.wait(20)
main()