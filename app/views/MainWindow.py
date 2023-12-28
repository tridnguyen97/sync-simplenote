from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QThreadPool, Slot
from datetime import datetime
from resources.views.MainWindow_ui import Ui_MainWindow
from app.services.login import simplenote, simplenote_login
from app.services.worker import Worker


class MainWindow(QMainWindow, Ui_MainWindow):
    """Main Window."""

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.note_list = []
        self.sm_obj = None
        self.thread_pool = QThreadPool()
        self.done_status = False
        self.login_btn.clicked.connect(self.on_signin)
    
    def on_get_note(self, progress_callback, done_callback):
        progress_callback.emit("getting notes")
        try:
            sync_notes, status = self.sm_obj.get_note_list(tags=['synctoolapi'])
            if status == 0:
                if len(sync_notes) > 0:
                    sync_note = sync_notes[0]
                    last_sync_datetime = datetime.fromtimestamp(sync_note['modificationDate'])  
                    note_list, status = self.sm_obj.get_note_list(
                            since=last_sync_datetime.date()
                        )
                    if status == 0:
                        self.note_list = note_list
                        sync_note['content'] = f'''
                            last updated: {datetime.now()}\n
                            {len(self.note_list)} note has been synced.
                        '''
                        self.sm_obj.update_note(sync_note)
                    else:
                        raise Exception
                else:
                    note_list, status = self.sm_obj.get_note_list()
                    if status == 0:
                        self.note_list = note_list
                        new_sync_note = {
                            'tags': ['synctoolapi'],
                            'content': f'''
                                last updated: {datetime.now()}\n
                                {len(self.note_list)} has been synced.
                            '''
                        }
                        self.sm_obj.add_note(new_sync_note)
            else:
                raise Exception
        except Exception as e:
            print(e)
        done_callback.emit(True)
        progress_callback.emit("done getting note")

    def on_signin(self):
        try:
            print("Signing in...")
            simplenote_object, token = simplenote_login(
                self.username_edit.text(), 
                self.password_edit.text()
            )
            if token:
                self.centralwidget.setCurrentWidget(self.home)
                self.sm_obj = simplenote_object
                progress_worker = Worker(self.on_get_note)
                self.thread_pool.start(progress_worker)
                progress_worker.signals.done.connect(self.load_info_view)
                progress_worker.signals.progress.connect(self.load_progress)

        except simplenote.SimplenoteLoginFailed as err:
            print(err.__traceback__)

    def load_info_view(self):
        print('info edit has been started')
        self.info_edit.setText(
            f'''
                last updated: {datetime.now()}\n
                {len(self.note_list)} note has been synced.
            '''
        )
    
    @Slot(str)
    def load_progress(self, progress):
        self.status_label.setText(progress)
