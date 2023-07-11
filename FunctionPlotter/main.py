from PySide2 import QtCore, QtWidgets , QtGui
from PySide2.QtWidgets import QPushButton ,QLineEdit ,QMessageBox 
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import numpy as np
import sys
import  os




class MainWindow(QtWidgets.QMainWindow):


    def __init__(self):

        super(MainWindow, self).__init__()
        self.setWindowTitle("Function Plotter")
        self.setWindowIcon(QtGui.QIcon("resources/plot.png"))
        self.msg= QMessageBox()
        self.setIconSize(QtCore.QSize(500, 500))
        self.main_widget = QtWidgets.QWidget(self)
        self.resize(900,600)
        self.InitLineEdit()  
        self.InitFig() 
        self.InitButton() 
        self.InitLayouts()

        self.axes.set_title("Function Plotter")

        self.setCentralWidget(self.main_widget)
        self.show()

    # This Function for layouts intialization
    def InitLayouts(self) :

        self.layout = QtWidgets.QGridLayout(self.main_widget)
        self.layout.addWidget(self.EquationText,0,0)
        self.layout.addWidget(self.x1,0,1)
        self.layout.addWidget(self.x2,0,2)
        self.layout.addWidget(self.PlotButton,0,3)
        self.EquationText.setMinimumHeight(40)
        self.PlotButton.setMinimumHeight(35)
        self.x1.setMinimumHeight(30)
        self.x2.setMinimumHeight(30)
        self.x1.setMaximumWidth(130)
        self.x2.setMaximumWidth(150)    

        self.layout.addWidget(self.canvas,2,0,2,4)
        self.layout.setHorizontalSpacing(20)
        self.layout.setMargin(20)
        


     
    # This Function for Line Edit style
    def InitLineEdit(self):
        self.EquationText= QLineEdit(self)
        self.EquationText.setToolTip("e.g. 3*x^2 + 1/x")
        self.EquationText.setStyleSheet("background-color: white;")
        self.x1= QLineEdit(self)
        self.x2= QLineEdit(self)
        self.x1.setStyleSheet("background-color: white;")
        self.x2.setStyleSheet("background-color: white;")

        font = self.EquationText.font()      
        font.setPointSize(15)               
        self.EquationText.setFont(font)
        self.EquationText.setPlaceholderText("  F(x) = ")
        self.x1.setPlaceholderText(" Min x= ")
        self.x2.setPlaceholderText(" Max x= ")
        self.equation = str(self.EquationText.text())

    # This Function for Adding Plot figure
    def InitFig(self):
        self.fig = Figure()
        self.axes = self.fig.add_subplot(111)
        self.canvas = FigureCanvas(self.fig)

    # This Function For Button style
    def InitButton(self):
        self.PlotButton = QPushButton("Plot",self)
        self.PlotButton.setToolTip("Plot")
        self.PlotButton.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.PlotButton.clicked.connect(self.plotFunc)
        self.PlotButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

    # This Function For input validation message style
    def inputValidation(self):
        self.msg.setWindowTitle("INVALID INPUT")
        self.msg.setWindowIcon(QtGui.QIcon("resources/plot.png"))
        self.msg.setIcon(QMessageBox.Warning)
        x = self.msg.exec_()

    # This Function For Plotting Function
    def plotFunc(self):
        try:
            self.axes.clear()
            self.equation = str(self.EquationText.text()).lower()
            inp = self.equation
            title = inp.replace("*","")
        
            x1= int(self.x1.text())
            x2= int(self.x2.text())
            if(x1 > x2):
                self.msg.setText("Min x should be less than Max x")
                self.inputValidation()
            else :
                x = np.linspace(x1, x2) 
                expr = inp.replace("^","**")
                self.axes.set_title("$"+title+"$")
                y= eval(expr)
                self.axes.plot(x,y)
                self.fig.canvas.draw()
        except :
            if not (self.x1.text().isdecimal() ) or not ( self.x2.text().isdecimal() )  :
                self.msg.setText("invalid number! , Please enter integer numbers only")
            
            else :
                self.msg.setText("Please enter a valid univariate polynomial equation\n e.g. 3*x^2 + 1/x ")

            
            self.inputValidation()




if __name__ == '__main__':
    
    os.chdir(os.path.dirname(os.path.abspath(__file__))) 
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.setStyleSheet("background-color: rgb(49, 49, 49);;") 
    w.show()
    app.exec_()
    