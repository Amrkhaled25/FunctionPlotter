import pytest
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtWidgets import QMessageBox
from main import MainWindow

@pytest.fixture
def main_window(qtbot):
    window = MainWindow()
    qtbot.addWidget(window)
    return window

# Test if program executed successfully 
def test_program_execution(qtbot, main_window):
    plot_button = main_window.PlotButton
    qtbot.mouseClick(plot_button, QtCore.Qt.LeftButton)
    assert main_window.isVisible()


#Test Plot Button
def test_plot_button_click(qtbot, main_window):
    equation_text = main_window.EquationText
    equation_text.setText("x^2")
    x1_text = main_window.x1
    x1_text.setText("0")
    x2_text = main_window.x2
    x2_text.setText("10")

    plot_button = main_window.PlotButton
    qtbot.mouseClick(plot_button, QtCore.Qt.LeftButton)

    assert main_window.axes.get_title() == "$x^2$"

    message_box = main_window.msg
    message_box.close()

#Test invalid input from Equation text
def test_invalid_input_equation(qtbot, main_window):
    equation_text = main_window.EquationText
    x1_text = main_window.x1
    x2_text = main_window.x2

    
    qtbot.keyClicks(equation_text, "x^2 + y")
    assert equation_text.text() == "x^2 + y"

    
    qtbot.keyClicks(x1_text, "1")
    assert x1_text.text() == "1"

    
    qtbot.keyClicks(x2_text, "10")
    assert x2_text.text() == "10"

    plot_button = main_window.PlotButton
    qtbot.mouseClick(plot_button, QtCore.Qt.LeftButton)

    message_box = main_window.msg
    assert message_box.text() == "Please enter a valid univariate polynomial equation\n e.g. 3*x^2 + 1/x "
    assert message_box.icon() == QMessageBox.Warning

    message_box.close()

#Test invalid input from numbers Edit Line
def test_invalid_input_numbers(qtbot, main_window):
    equation_text = main_window.EquationText
    x1_text = main_window.x1
    x2_text = main_window.x2

    
    qtbot.keyClicks(equation_text, "x^2")
    assert equation_text.text() == "x^2"

    
    qtbot.keyClicks(x1_text, "7")
    assert x1_text.text() == "7"

    
    qtbot.keyClicks(x2_text, "1")
    assert x2_text.text() == "1"

    plot_button = main_window.PlotButton
    qtbot.mouseClick(plot_button, QtCore.Qt.LeftButton)

    message_box = main_window.msg
    assert message_box.text() == "Min x should be less than Max x"
    assert message_box.icon() == QMessageBox.Warning

    message_box.close()


if __name__ == '__main__':
    pytest.main(['-v'])
