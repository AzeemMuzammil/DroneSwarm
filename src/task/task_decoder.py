from enum import Enum

from task.tasks import TakeOffTask, GoToTask, WaitTask, LandTask, PreCondition
from utils import Constants


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

    def get_tasks(self, json_data):
        global TASK_TYPE

        task_models = []

        for json_obj in json_data:
            if json_obj[Constants.TASK_TYPE] == TaskType.translate_to_string(TaskType.TAKE_OFF):
                pre_conditions = json_obj[Constants.PRE_CONDITIONS] if Constants.PRE_CONDITIONS in json_obj else None
                pre_conditions_lst = None
                if pre_conditions is not None:
                    pre_conditions_lst = []
                    for condition in pre_conditions:
                        pre_condition = PreCondition(
                            condition[Constants.PRE_CONDITION_TASK_ID], condition[Constants.PRE_CONDITION_TASK_STATUS])
                        pre_conditions_lst.append(pre_condition)

                task_model = TakeOffTask(
                    json_obj[Constants.TASK_MODE], json_obj[Constants.TASK_ID], json_obj[Constants.TAKE_OFF_HEIGHT], pre_conditions_lst)
                task_models.append(task_model)
            if json_obj[Constants.TASK_TYPE] == TaskType.translate_to_string(TaskType.GO_TO):
                pre_conditions = json_obj[Constants.PRE_CONDITIONS] if Constants.PRE_CONDITIONS in json_obj else None
                pre_conditions_lst = None
                if pre_conditions is not None:
                    pre_conditions_lst = []
                    for condition in pre_conditions:
                        pre_condition = PreCondition(
                            condition[Constants.PRE_CONDITION_TASK_ID], condition[Constants.PRE_CONDITION_TASK_STATUS])
                        pre_conditions_lst.append(pre_condition)

                next_loc = json_obj[Constants.NEXT_LOCATION]
                task_model = GoToTask(
                    json_obj[Constants.TASK_MODE], json_obj[Constants.TASK_ID], next_loc[Constants.NORTH], next_loc[Constants.EAST], next_loc[Constants.ALTITUDE], pre_conditions_lst)
                task_models.append(task_model)
            if json_obj[Constants.TASK_TYPE] == TaskType.translate_to_string(TaskType.WAIT):
                pre_conditions = json_obj[Constants.PRE_CONDITIONS] if Constants.PRE_CONDITIONS in json_obj else None
                pre_conditions_lst = None
                if pre_conditions is not None:
                    pre_conditions_lst = []
                    for condition in pre_conditions:
                        pre_condition = PreCondition(
                            condition[Constants.PRE_CONDITION_TASK_ID], condition[Constants.PRE_CONDITION_TASK_STATUS])
                        pre_conditions_lst.append(pre_condition)

                task_model = WaitTask(
                    json_obj[Constants.TASK_MODE], json_obj[Constants.TASK_ID], json_obj[Constants.WAIT_TIME], pre_conditions_lst)
                task_models.append(task_model)
            if json_obj[Constants.TASK_TYPE] == TaskType.translate_to_string(TaskType.LAND):
                pre_conditions = json_obj[Constants.PRE_CONDITIONS] if Constants.PRE_CONDITIONS in json_obj else None
                pre_conditions_lst = None
                if pre_conditions is not None:
                    pre_conditions_lst = []
                    for condition in pre_conditions:
                        pre_condition = PreCondition(
                            condition[Constants.PRE_CONDITION_TASK_ID], condition[Constants.PRE_CONDITION_TASK_STATUS])
                        pre_conditions_lst.append(pre_condition)

                task_model = LandTask(
                    json_obj[Constants.TASK_MODE], json_obj[Constants.TASK_ID], pre_conditions_lst)
                task_models.append(task_model)

        return task_models
