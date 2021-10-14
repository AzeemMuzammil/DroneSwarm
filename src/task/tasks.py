# Class which defines preconditions for each task

class PreCondition:

    def __init__(self, task_id: int, task_status: str):
        self.task_id = task_id
        self.task_status = task_status


# Classes for all types of Tasks

class TakeOffTask:

    def __init__(self, mode: str, task_id: int, height: float, pre_conditions: list):
        self.mode = mode
        self.task_id = task_id
        self.height = height
        self.pre_conditions = pre_conditions


class GoToTask:

    def __init__(self, mode: str, task_id: int, north: float, east: float, alt: float, pre_conditions: list):
        self.mode = mode
        self.task_id = task_id
        self.north = north
        self.east = east
        self.alt = alt
        self.pre_conditions = pre_conditions


class WaitTask:

    def __init__(self, mode: str, task_id: int, wait_time: int, pre_conditions: list):
        self.mode = mode
        self.task_id = task_id
        self.wait_time = wait_time
        self.pre_conditions = pre_conditions


class LandTask:

    def __init__(self, mode: str, task_id: int, pre_conditions: list):
        self.mode = mode
        self.task_id = task_id
        self.pre_conditions = pre_conditions
