import time

time.sleep(3)

f = open("file/text.txt", "a")
f.write('d-1 ')
f.close()

while True:
    f = open("file/text.txt", "r")
    op = f.read()
    f.close()
    op = op.split(" ")
    if len(op) == 3:
        break
    time.sleep(0.01)