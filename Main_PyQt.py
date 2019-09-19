
from OpenGL.GL import *
from OpenGL.GLU import *
import random




import sys,time

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
from PyQt5.uic import *
from PyQt5 import QtCore


class mainWindow(QMainWindow):
    radius = 0.7
    L = 10
    sclip = 50
    verticies = (
        (L, -L, -L),
        (L, L, -L),
        (-L, L, -L),
        (-L, -L, -L),
        (L, -L, L),
        (L, L, L),
        (-L, -L, L),
        (-L, L, L)
    )
    edges = (
        (0, 1),
        (0, 3),
        (0, 4),
        (2, 1),
        (2, 3),
        (2, 7),
        (6, 3),
        (6, 4),
        (6, 7),
        (5, 1),
        (5, 4),
        (5, 7)
    )

    def __init__(self, *args):

        super(mainWindow, self).__init__(*args)
        loadUi('UI.ui', self)
        self.ini_flag=0

    def Cube(self):
        glBegin(GL_LINES)

        for edge in self.edges:
            for vertex in edge:
                glColor3fv((0, 0.5, 0.8))
                glVertex3fv(self.verticies[vertex])
        glEnd()

    def points(self,number):
        px = []
        py = []
        pz = []
        for i in range(number):
            x = random.uniform(-self.L + self.radius, self.L - self.radius)
            y = random.uniform(-self.L + self.radius, self.L - self.radius)
            z = random.uniform(-self.L + self.radius, self.L - self.radius)
            px.append(x)
            py.append(y)
            pz.append(z)
        return px, py, pz

    def update_position(self,value):
        increment = 1
        nn = random.randint(-1, 1)
        value += nn * increment
        if (value < -self.L + self.radius):
            value = -self.L + self.radius
        if (value > self.L - self.radius):
            value = self.L - self.radius
        return value

    def random_Spheres(self,number):
        for i in range(number):
            glPushMatrix()
            glMaterialfv(GL_FRONT, GL_DIFFUSE, (1, 0, 0))
            quadratic = gluNewQuadric()
            ppx[i] = self.update_position(ppx[i])
            ppy[i] = self.update_position(ppy[i])
            ppz[i] = self.update_position(ppz[i])
            glTranslatef(ppx[i], ppy[i], ppz[i])
            glRotatef(20, 30, -20, 0)
            glColor3fv((0.2, 0.8, 0.2))
            gluSphere(quadratic, self.radius, self.sclip, self.sclip)
            glPopMatrix()
    def setupUI(self):
        self.openGLWidget.initializeGL()
        self.slider_x=self.x_axis
        self.slider_y = self.y_axis
        self.slider_z = self.z_axis
        self.slider_x.valueChanged.connect(self.valuechangex)
        self.slider_y.valueChanged.connect(self.valuechangey)
        self.slider_z.valueChanged.connect(self.valuechangez)
        #self.openGLWidget.resizeGL(651,551)
        self.openGLWidget.paintGL = self.paintGL
        # self.timer = QtCore.QTimer()
        # self.timer.timeout.connect(self.timerEvent)
        # self.timer.start(100)
        #app.exec_()
        #self.openGLWidget.update
        timer = QTimer(self)
        timer.timeout.connect(self.openGLWidget.update)
        timer.start(100)
    def valuechangex(self):
        global px, py, pz
        val=self.slider_x.value()
        px=float(val)/10.0
        if (px < -self.L + self.radius):
            px = -self.L + self.radius
        self.x_val.setText("%.2f" % px)
        self.slider_x.setValue(int(px * 10))
    def valuechangey(self):
        global px, py, pz
        val=self.slider_y.value()
        py=float(val)/10.0
        if (py < -self.L + self.radius):
            py = -self.L + self.radius
        self.y_val.setText("%.2f" % py)
        self.slider_y.setValue(int(py * 10))
    def valuechangez(self):
        global px, py, pz
        val=self.slider_z.value()
        pz=float(val)/10.0
        if (pz < -self.L + self.radius):
            pz = -self.L + self.radius
        self.z_val.setText("%.2f" % pz)
        self.slider_z.setValue(int(pz * 10))
    def onKeyPress(self, event):
        print(event.key)

    def keyPressEvent(self, event):
        # print(event.key())
        global px, py, pz, increment
        if event.key() == Qt.Key_Escape:
            self.close()
        if event.key() == Qt.Key_A:
            px -= increment
            if (px < -self.L + self.radius):
                px = -self.L + self.radius
            self.x_val.setText("%.2f" % px)
            self.slider_x.setValue(int(px * 10))
        if event.key() == Qt.Key_D:
            px += increment
            if (px > self.L - self.radius):
                px = self.L - self.radius
            self.slider_x.setValue(int(px*10))
            self.x_val.setText("%.2f" %px)
        if event.key() == Qt.Key_M:
            py -= increment
            if (py < -self.L + self.radius):
                py = -self.L + self.radius
            self.y_val.setText("%.2f" % py)
            self.slider_y.setValue(int(py * 10))
        if event.key() == Qt.Key_N:
            py += increment
            if (py > self.L - self.radius):
                py = self.L - self.radius
            self.slider_y.setValue(int(py*10))
            self.y_val.setText("%.2f" %py)
        if event.key() == Qt.Key_S:
            pz -= increment
            if (pz < -self.L + self.radius):
                pz = -self.L + self.radius
            self.z_val.setText("%.2f" % pz)
            self.slider_z.setValue(int(pz * 10))
        if event.key() == Qt.Key_W:
            pz += increment
            if (pz > self.L - self.radius):
                pz = self.L - self.radius
            self.slider_z.setValue(int(pz*10))
            self.z_val.setText("%.2f" %pz)

    def paintGL(self):
        global px, py, pz, increment
        global ppx, ppy, ppz
        number = 10
        if(self.ini_flag==0):


            px = 0.0
            py = 0.0
            pz = 0.0
            increment = 0.1
            ppx, ppy, ppz = self.points(number)
            gluPerspective(1, (1.0), 0.1, 2500.0)
            glTranslatef(0.0, 0, -2000)
            glRotatef(20, 30, -20, 0)
            self.ini_flag =1
        # create cube
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.Cube()
        # create main Sphere
        glPushMatrix()
        glMaterialfv(GL_FRONT, GL_DIFFUSE, (1, 0, 0))
        quadratic = gluNewQuadric()
        glTranslatef(px, py, pz)
        glRotatef(20, 30, -20, 0)
        glColor3fv((1, 0, 0))
        gluSphere(quadratic, self.radius, self.sclip, self.sclip)
        glPopMatrix()
        self.random_Spheres(number)
        # glEnd()
        # glFlush()
        time.sleep(1)
        #glEnd()
        # while True:
        #     # stop event
        #     for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             pygame.quit()
        #             quit()
        #     # key pressed event
        #     keys = pygame.key.get_pressed()
        #     if keys[K_LEFT]:
        #         px += increment
        #         if (px > L - radius):
        #             px = L - radius
        #     elif keys[K_RIGHT]:
        #         px -= increment
        #         if (px < -L + radius):
        #             px = -L + radius
        #     elif keys[K_UP]:
        #         pz += increment
        #         if (pz > L - radius):
        #             pz = L - radius
        #     elif keys[K_DOWN]:
        #         pz -= increment
        #         if (pz < -L + radius):
        #             pz = -L + radius
        #     elif keys[K_n]:
        #         py += increment
        #         if (py > L - radius):
        #             py = L - radius
        #     elif keys[K_m]:
        #         py -= increment
        #         if (py < -L + radius):
        #             py = -L + radius





app = QApplication(sys.argv)
window = mainWindow()
window.setupUI()
window.show()
sys.exit(app.exec_())





