import os
from multiprocessing import Process,Queue

# os.system('python3 main.py')
# os.system('python3 main_1.py')
# os.system('python3 main_2.py')
# os.system('python3 main_3.py')


tasks = ("python3 main.py",\
"python3 main_1.py",\
"python3 main_2.py",\
"python3 main_3.py")

def worker():
    while True:
        item = q.get()
        os.system(item)

q = Queue()
for i in tasks:
     t = Process(target=worker)
     t.start()

for item in tasks:
    q.put(item)

# q.join()  