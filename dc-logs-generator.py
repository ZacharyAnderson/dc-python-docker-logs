import threading
import time


def log_generator():
    print("Log Time - " + time.ctime())
    thread = threading.Timer(60.0, log_generator)
    thread.start()


log_generator()
