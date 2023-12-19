from PySide6.QtWidgets import QMainWindow
from resources.views.MainWindow_ui import Ui_MainWindow
from app.services.login import simplenote, simplenote_login


class MainWindow(QMainWindow, Ui_MainWindow):
    """Main Window."""

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.note_list = []
        self.login_btn.clicked.connect(self.on_signin)

    def on_signin(self):
        try:
            print("Signing in...")
            simplenote_instance, token = simplenote_login(
                self.username_edit.text(), 
                self.password_edit.text()
            )
            if token:
                self.centralwidget.setCurrentWidget(self.home)
            # if self.simplenote_instance isinstance(simplenote):
        except simplenote.SimplenoteLoginFailed as err:
            print(err.__traceback__)
