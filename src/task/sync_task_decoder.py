from task.sync_tasks import SyncTakeOffTask, SyncGoToTask, SyncWaitTask, SyncLandTask
from task.tasks import PreCondition
from task.task_decoder import TaskType
from utils import Constants


class SyncTaskDecoder:

    def get_tasks(self, json_data):
        global TASK_TYPE

        task_models = []

        for json_obj in json_data:
            if json_obj[Constants.TASK_TYPE] == TaskType.translate_to_string(TaskType.SYNC_TAKE_OFF):
                pre_conditions = json_obj[Constants.PRE_CONDITIONS] if Constants.PRE_CONDITIONS in json_obj else None
                pre_conditions_lst = None
                if pre_conditions is not None:
                    pre_conditions_lst = []
                    for condition in pre_conditions:
                        pre_condition = PreCondition(
                            condition[Constants.PRE_CONDITION_TASK_ID], condition[Constants.PRE_CONDITION_TASK_STATUS])
                        pre_conditions_lst.append(pre_condition)

                task_model = SyncTakeOffTask(
                    json_obj[Constants.TASK_MODE], json_obj[Constants.TASK_ID], json_obj[Constants.TAKE_OFF_HEIGHT], pre_conditions_lst, send)
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
