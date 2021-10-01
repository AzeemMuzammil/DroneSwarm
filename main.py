# import asyncio
# import math

# from mavsdk import System
# from mavsdk.offboard import (OffboardError, VelocityNedYaw, PositionNedYaw)
# from mavsdk.telemetry import Position, FlightMode
# from src import TaskDecoder, TaskType, TakeOffTask, GoToTask, LandTask


# models = TaskDecoder().get_tasks()

# # for model in models:
# #     if type(models[0]) == TakeOffTask:
# #         task = models[0]

# async def takeoff(drone, height):
#     await drone.action.set_takeoff_altitude(height + 1)

#     print("-- drone is taking off --")
#     await drone.action.takeoff()

#     async for position in drone.telemetry.position():
#         if (position.relative_altitude_m > height * 0.98):
#             await asyncio.sleep(0.01)
#             break
    
#     print(f"-- drone reached the altitude of {height}m --")

# async def goto(drone, north, east, alt):
#     print(f"-- drone is moving to ({north}, {east}, {alt})--")
#     await drone.offboard.set_position_ned(PositionNedYaw(north, east, -alt, 0))
#     await asyncio.sleep(5)

# async def land(drone):
#     print("-- drone is landing")
#     await drone.action.land()
#     print("-- drone landed")


# async def run():

#     drone = System()
#     await drone.connect(system_address="udp://:14540")

#     print("Waiting for drone to connect...")
#     async for state in drone.core.connection_state():
#         if state.is_connected:
#             print(f"Drone discovered!")
#             break

#     print("-- Arming")
#     await drone.action.arm()

#     for model in models:
#         if type(model) == TakeOffTask:
#             await takeoff(drone, model.height)
        
#         if type(model) == GoToTask:
#             current_flight_mode = None
#             async for flight_mode in drone.telemetry.flight_mode():
#                 current_flight_mode = flight_mode
#                 break
            
#             if current_flight_mode != FlightMode.OFFBOARD:
#                 print("-- setting initial setpoint")
#                 await drone.offboard.set_position_ned(PositionNedYaw(0.0, 0.0, 0.0, 0.0))

#                 print("-- Starting offboard")
#                 try:
#                     await drone.offboard.start()
#                 except OffboardError as error:
#                     print(f"Starting offboard mode failed with error code: \
#                         {error._result.result}")
#                     print("-- Disarming")
#                     await drone.action.disarm()
#                     return
            
#             await goto(drone, model.north, model.east, model.alt)
        
#         if type(model) == LandTask:
#             current_flight_mode = None
#             async for flight_mode in drone.telemetry.flight_mode():
#                 current_flight_mode = flight_mode
#                 break

#             if current_flight_mode != FlightMode.OFFBOARD:
#                 print("-- Stopping offboard")
#                 try:
#                     await drone.offboard.stop()
#                 except OffboardError as error:
#                     print(f"Stopping offboard mode failed with error code: \
#                         {error._result.result}")

#             await land(drone)

# if __name__ == "__main__":
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(run())


import watchdog.events
import watchdog.observers
import time

class Handler(watchdog.events.PatternMatchingEventHandler):
    def __init__(self):
        # Set the patterns for PatternMatchingEventHandler
        watchdog.events.PatternMatchingEventHandler.__init__(self, patterns=['*.json'],
                                                             ignore_directories=True, case_sensitive=False)
  
    def on_created(self, event):
        print("Watchdog received created event - % s." % event.src_path)
        # Event is created, you can process it now
  
    def on_modified(self, event):
        print("Watchdog received modified event - % s." % event.src_path)
        # Event is modified, you can process it now
  
  
if __name__ == "__main__":
    src_path = "src/tasks/"
    event_handler = Handler()
    observer = watchdog.observers.Observer()
    observer.schedule(event_handler, path=src_path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Keyboard Interrupt")
        observer.stop()
    observer.join()