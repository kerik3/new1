import sys
import random
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QPushButton, QGraphicsView, QGraphicsScene, QGraphicsEllipseItem
)
from PyQt6.QtGui import QColor, QBrush


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Круги")
        self.setGeometry(100, 100, 600, 400)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)
        self.btn_add = QPushButton("Добавить окружность")
        self.layout.addWidget(self.btn_add)
        self.graphics_view = QGraphicsView()
        self.layout.addWidget(self.graphics_view)
        self.scene = QGraphicsScene()
        self.graphics_view.setScene(self.scene)
        self.btn_add.clicked.connect(self.add_circle)

    def add_circle(self):
        diameter = random.randint(20, 100)
        color = QColor(
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )

        view_width = self.graphics_view.width() - diameter - 20
        view_height = self.graphics_view.height() - diameter - 20
        x = random.randint(10, max(20, view_width))
        y = random.randint(10, max(20, view_height))

        circle = QGraphicsEllipseItem(x, y, diameter, diameter)
        circle.setBrush(QBrush(color))

        self.scene.addItem(circle)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
