from enum import Enum
import json


class TaskType(Enum):

    TAKE_OFF = 0
    LAND = 1
    GO_TO = 2
    WAIT = 3

    def translate_to_string(self) -> str:
        if self == TaskType.TAKE_OFF:
            return "TAKE_OFF"
        if self == TaskType.LAND:
            return "LAND"
        if self == TaskType.GO_TO:
            return "GO_TO"
        if self == TaskType.WAIT:
            return "WAIT"

    def translate_from_string(task_type_val: str):
        if task_type_val == "TAKE_OFF":
            return TaskType.TAKE_OFF
        if task_type_val == "LAND":
            return TaskType.LAND
        if task_type_val == "GO_TO":
            return TaskType.GO_TO
        if task_type_val == "WAIT":
            return TaskType.WAIT

    def __str__(self):
        return self.name


class TaskMode(Enum):

    SEQ = 0
    VUT = 1
    NUT = 2

    def translate_to_string(self):
        if self == TaskMode.SEQ:
            return "SEQ"
        if self == TaskMode.VUT:
            return "VUT"
        if self == TaskMode.NUT:
            return "NUT"

    def translate_from_string(self):
        if self == "SEQ":
            return TaskType.SEQ
        if self == "VUT":
            return TaskType.VUT
        if self == "NUT":
            return TaskType.NUT

    def __str__(self):
        return self.name


class TaskDecoder:

    def get_tasks(self):
        json_file = open('src/tasks/main.json', "r")

        json_data = json.loads(json_file.read())

        task_models = []

        for json_obj in json_data:
            if json_obj['taskType'] == 'TAKE_OFF':
                task_model = TakeOffTask(json_obj['taskMode'], json_obj['taskId'], json_obj['heightInMeters'])
                task_models.append(task_model)
            if json_obj['taskType'] == 'LAND':
                task_model = LandTask(json_obj['taskMode'], json_obj['taskId'])
                task_models.append(task_model)
            if json_obj['taskType'] == 'GO_TO':
                next_loc = json_obj['nextLocation']
                task_model = GoToTask(json_obj['taskMode'], json_obj['taskId'], next_loc['north'], next_loc['east'], next_loc['alt'])
                task_models.append(task_model)

        json_file.close()

        return task_models


class TakeOffTask:

    def __init__(self, mode: str, task_id: int, height: float):
        self.mode = mode
        self.task_id = task_id
        self.height = height


class GoToTask:

    def __init__(self, mode: str, task_id: int, north: float, east: float, alt: float):
        self.mode = mode
        self.task_id = task_id
        self.north = north
        self.east = east
        self.alt = alt


class LandTask:

    def __init__(self, mode: str, task_id: int):
        self.mode = mode
        self.task_id = task_id
