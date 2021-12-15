# import watchdog.events
# import watchdog.observers
import time

time.sleep(2)

f = open("file/text.txt", "a")
f.write('d-2 ')
f.close()

while True:
    f = open("file/text.txt", "r")
    op = f.read()
    f.close()
    op = op.split(" ")
    if len(op) == 3:
        break
    time.sleep(0.01)
        

# class Handler(watchdog.events.PatternMatchingEventHandler):
#     def __init__(self):
#         # Set the patterns for PatternMatchingEventHandler
#         watchdog.events.PatternMatchingEventHandler.__init__(self, patterns=['*.txt'],
#                                                              ignore_directories=True, case_sensitive=False)

#     def on_created(self, event):
#         print("Watchdog received created event - % s." % event.src_path)
#         # Event is created, you can process it now

#     def on_modified(self, event):
#         print("Watchdog received modified event - % s." % event.src_path)
#         f = open("file/text.txt", "r")
#         for x in f:
#             print(x)
#         # Event is modified, you can process it now


# if __name__ == "__main__":
#     src_path = "file/"
#     event_handler = Handler()
#     observer = watchdog.observers.Observer()
#     observer.schedule(event_handler, path=src_path, recursive=True)
#     observer.start()
#     try:
#         while True:
#             time.sleep(1)
#     except KeyboardInterrupt:
#         print("Keyboard Interrupt")
#         observer.stop()
#     observer.join()