from communication import Sender
import time

comm = Sender(6000)
comm.connect()
comm.send_data("hi")

time.sleep(2)
comm.send_data("hi2")
comm.disconnect()
