import asyncio
import math

from mavsdk import System
from mavsdk.offboard import (OffboardError, VelocityNedYaw, PositionNedYaw)
from mavsdk.telemetry import Position, FlightMode


class TaskExecutor:

    async def takeoff(drone, height):
        await drone.action.set_takeoff_altitude(height + 1)

        print("-- drone is taking off --")
        await drone.action.takeoff()

        async for position in drone.telemetry.position():
            if (position.relative_altitude_m > height * 0.98):
                await asyncio.sleep(0.01)
                break

        print(f"-- drone reached the altitude of {height}m --")

    async def sync_takeoff(drone, height):
        await drone.action.set_takeoff_altitude(height + 1)

        print("-- drone is taking off (Sync) --")
        await drone.action.takeoff()

        async for position in drone.telemetry.position():
            if (position.relative_altitude_m > height * 0.98):
                await asyncio.sleep(0.01)
                break

        # await drone.action.
