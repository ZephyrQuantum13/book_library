import sys
from PyQt6.QtWidgets import QApplication
from ui.main_window import MainWindow

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Book Library")

    window = MainWindow()
    window.show()

    return app.exec() 
    
if __name__ == "__main__":
    main()