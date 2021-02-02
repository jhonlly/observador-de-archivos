import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import pync
import os

class Watcher:

    def __init__(self):
        self.observer = Observer()
        
    def run(self, directorio_a_observar ):
        manejador_eventos = Handler()
        self.observer.schedule(manejador_eventos,directorio_a_observar)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Error")
            
        self.observer.join()
    
    def stop(self):
        self.observer.stop()



class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            pync.notify("Se ha creado %s"% event.src_path, group=os.getpid())
            print("Received created event - %s." % event.src_path)
           

        elif event.event_type == 'modified':
            pync.notify("Se ha modificado %s"% event.src_path, group=os.getpid())
            print("Received modified event - %s." % event.src_path)


if __name__ == '__main__':
    w = Watcher()
    w.run()