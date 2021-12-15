import asyncio
import math

from mavsdk import System
from mavsdk.offboard import (OffboardError, VelocityNedYaw, PositionNedYaw)
from mavsdk.telemetry import Position, FlightMode, PositionNed
from src.task import TaskDecoder, TaskType, TakeOffTask, GoToTask, LandTask
from src.task import SyncWaitTask

import json

from src.task.tasks import WaitTask
json_file = open('task_file/main_6.json', "r")
json_data = json.loads(json_file.read())


models = TaskDecoder().get_tasks(json_data)

def get_location_offset_meters(original_location, dNorth, dEast, alt):
    earth_radius = 6378137.0 #Radius of "spherical" earth
    #Coordinate offsets in radians
    dLat = dNorth / earth_radius
    dLon = dEast / (earth_radius *math.cos(math.pi * original_location.latitude_deg / 180))

    #New position in decimal degrees
    new_lat = original_location.latitude_deg + (dLat * 180 / math.pi)
    new_lon = original_location.longitude_deg + (dLon * 180 / math.pi)
    new_alt = original_location.absolute_altitude_m + alt
    new_relative_alt = original_location.relative_altitude_m + alt
    return Position(new_lat, new_lon, new_alt, new_relative_alt)

async def takeoff(drone, height):
    await drone.action.set_takeoff_altitude(height)

    print("-- drone is taking off --")
    await drone.action.takeoff()

    async for position in drone.telemetry.position():
        if (position.relative_altitude_m > height * 0.98):
            break

    print(f"-- drone reached the altitude of {height}m --")

async def goto(drone, north, east, alt):
    print(f"-- drone is moving to ({north}, {east}, {alt})--")
    await drone.offboard.set_position_ned(PositionNedYaw(north, east, -alt, 0))

    async for position_velocity in drone.telemetry.position_velocity_ned():
        position = position_velocity.position
        if ((position.north_m > north - 0.1) and (position.north_m < north + 0.1)) and ((position.east_m > east - 0.1) and (position.east_m < east + 0.1)) and ((position.down_m < -alt + 0.1) and (position.down_m > -alt - 0.1) ):
            break
    
    # await asyncio.sleep(5)

    # async for position_velocity in drone.telemetry.position_velocity_ned():
    #     print(position_velocity.position)
    #     break
    
    print(f"-- drone reached the position ({north}, {east}, {alt})--")

async def wait(drone, time):
    print(f"-- drone is waiting for ({time})--")
    current_position = None

    async for position_velocity in drone.telemetry.position_velocity_ned():
        current_position = position_velocity.position
        break

    await drone.offboard.set_position_ned(PositionNedYaw(current_position.north_m, current_position.east_m, current_position.down_m, 0))
    await asyncio.sleep(time)
    print(f"-- drone waited for ({time})--")

async def sync_wait(drone, time):
    print(f"-- drone is waiting for ({time})--")
    current_position = None

    async for position_velocity in drone.telemetry.position_velocity_ned():
        current_position = position_velocity.position
        break

    await drone.offboard.set_position_ned(PositionNedYaw(current_position.north_m, current_position.east_m, current_position.down_m, 0))
    await asyncio.sleep(time)

    f = open("task_file/sync_file.txt", "a")
    f.write('d-6 ')
    f.close()

    while True:
        f = open("task_file/sync_file.txt", "r")
        op = f.read()
        f.close()
        if len(op.split(" ")) == 7:
            break
        await asyncio.sleep(0.01)
    print(f"-- drone waited for ({time})--")

async def land(drone):
    print("-- drone is landing")
    await drone.action.land()
    print("-- drone landed")


async def run():

    # drone = System()
    # await drone.connect(system_address="udp://:14542")

    drone = System(mavsdk_server_address="localhost", port=50045)
    await drone.connect()

    await drone.param.set_param_int("NAV_RCL_ACT", 0)

    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"Drone discovered!")
            break

    print("-- Arming")
    await drone.action.arm()

    for model in models:
        if type(model) == TakeOffTask:
            await takeoff(drone, model.height)

        if type(model) == GoToTask:
            current_flight_mode = None
            async for flight_mode in drone.telemetry.flight_mode():
                current_flight_mode = flight_mode
                break

            if current_flight_mode != FlightMode.OFFBOARD:
                print("-- setting initial setpoint")
                await drone.offboard.set_position_ned(PositionNedYaw(0.0, 0.0, 0.0, 0.0))

                print("-- Starting offboard")
                try:
                    await drone.offboard.start()
                except OffboardError as error:
                    print(f"Starting offboard mode failed with error code: \
                        {error._result.result}")
                    print("-- Disarming")
                    await drone.action.disarm()
                    return

            await goto(drone, model.north, model.east, model.alt)

        if type(model) == LandTask:
            current_flight_mode = None
            async for flight_mode in drone.telemetry.flight_mode():
                current_flight_mode = flight_mode
                break

            if current_flight_mode != FlightMode.OFFBOARD:
                print("-- Stopping offboard")
                try:
                    await drone.offboard.stop()
                except OffboardError as error:
                    print(f"Stopping offboard mode failed with error code: \
                        {error._result.result}")

            await land(drone)
        
        if type(model) == WaitTask:
            await wait(drone, model.wait_time)
        if type(model) == SyncWaitTask:
            await sync_wait(drone, model.wait_time)
        

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())