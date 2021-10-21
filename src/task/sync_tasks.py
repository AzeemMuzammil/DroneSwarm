# Classes for all types of Sync Tasks

class SyncTakeOffTask:

    def __init__(self, mode: str, task_id: int, height: float, pre_conditions: list, senders: list, receivers: list):
        self.mode = mode
        self.task_id = task_id
        self.height = height
        self.pre_conditions = pre_conditions
        self.senders = senders
        self.receivers = receivers


class SyncGoToTask:

    def __init__(self, mode: str, task_id: int, north: float, east: float, alt: float, pre_conditions: list, senders: list, receivers: list):
        self.mode = mode
        self.task_id = task_id
        self.north = north
        self.east = east
        self.alt = alt
        self.pre_conditions = pre_conditions
        self.senders = senders
        self.receivers = receivers


class SyncWaitTask:

    def __init__(self, mode: str, task_id: int, wait_time: int, pre_conditions: list, senders: list, receivers: list):
        self.mode = mode
        self.task_id = task_id
        self.wait_time = wait_time
        self.pre_conditions = pre_conditions
        self.senders = senders
        self.receivers = receivers


class SyncLandTask:

    def __init__(self, mode: str, task_id: int, pre_conditions: list, senders: list, receivers: list):
        self.mode = mode
        self.task_id = task_id
        self.pre_conditions = pre_conditions
        self.senders = senders
        self.receivers = receivers
