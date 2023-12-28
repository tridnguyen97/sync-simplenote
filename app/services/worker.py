from PySide6.QtCore import QThreadPool, Signal, Slot, QRunnable, QObject

class WorkerSignals(QObject):
    progress = Signal(str)
    done = Signal(bool)
    result = Signal(object)

class Worker(QRunnable):
    def __init__(self, worker_fn, *args, **kwargs) -> None:
        super(Worker, self).__init__()
        self.signals = WorkerSignals()
        self.fn = worker_fn
        self.args = args
        self.kwargs = kwargs
        kwargs['progress_callback'] = self.signals.progress
        kwargs['done_callback'] = self.signals.done
    
    @Slot(object)
    def run(self):
        self.fn(*self.args, **self.kwargs)