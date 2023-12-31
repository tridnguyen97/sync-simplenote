import sys

from PySide6.QtGui import QFontDatabase, QFont, QIcon
from PySide6.QtCore import QFile, QTextStream, QTranslator, QLocale
from PySide6.QtWidgets import QApplication

from app.views.MainWindow import MainWindow


def main():
    app = QApplication(sys.argv)

    app.setWindowIcon(QIcon(":/icons/app.svg"))

    fontDB = QFontDatabase()
    fontDB.addApplicationFont(":/fonts/Lato-Regular.ttf")
    app.setFont(QFont("Lato"))

    f = QFile(":/style.qss")
    f.open(QFile.ReadOnly | QFile.Text)
    app.setStyleSheet(QTextStream(f).readAll())
    f.close()

    translator = QTranslator()
    translator.load(":/translations/" + QLocale.system().name() + ".qm")
    app.installTranslator(translator)

    mw = MainWindow()
    mw.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
