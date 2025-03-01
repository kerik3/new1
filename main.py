import random
import sys

from PyQt6.QtGui import QColor, QBrush
from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsEllipseItem
from PyQt6.uic import loadUi


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("UI.ui", self)
        self.scene = QGraphicsScene()
        self.graphicsView.setScene(self.scene)
        self.btnAddCircle.clicked.connect(self.add_circle)

    def add_circle(self):
        diameter = random.randint(20, 100)
        x = random.randint(0, self.graphicsView.width() - diameter)
        y = random.randint(0, self.graphicsView.height() - diameter)
        circle = QGraphicsEllipseItem(x, y, diameter, diameter)
        circle.setBrush(QBrush(QColor(255, 255, 0)))
        self.scene.addItem(circle)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
