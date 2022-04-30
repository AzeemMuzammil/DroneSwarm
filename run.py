import os
from multiprocessing import Process,Queue
import threading
import subprocess
# os.system('python3 main.py')
# os.system('python3 main_1.py')
# os.system('python3 main_2.py')
# os.system('python3 main_3.py'), "python3 main_4.py","python3 main_5.py","python3 main_6.py",




scripts = (
"python3 main_1.py",\
"python3 main_2.py",\
"python3 main_3.py","python3 main_4.py")

scripts1 = (
"/home/halaldeen-ms/dev/DroneSwarm/main_1.py",\
"/home/halaldeen-ms/dev/DroneSwarm/main_2.py",\
"/home/halaldeen-ms/dev/DroneSwarm/main_3.py","/home/halaldeen-ms/dev/DroneSwarm/main_4.py",
"/home/halaldeen-ms/dev/DroneSwarm/main_5.py","/home/halaldeen-ms/dev/DroneSwarm/main_6.py")



def worker():
    while True:
        item = q.get()
        os.system(item)

q = Queue()
for i in scripts:
     t = Process(target=worker)
     t.start()

for item in scripts:
    q.put(item)

#q.join()  


# processes = []


# for script in scripts:
#     p = subprocess.Popen(["python3" ,scripts1])
#     processes.append(p)

# for p in processes:
#     p.wait()



