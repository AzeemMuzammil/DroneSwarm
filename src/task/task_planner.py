from os import remove
from .tasks import *
from .task_decoder import *

from random import randint


class TaskPlanner:
    # NUT tasks and VUT tasks will never have pre conditions

    def __compare_task(self, task_one, task_two):
        if (task_one.mode == task_two.mode):
            if (task_one.mode == TaskMode.translate_to_string(TaskMode.VUT) or task_one.mode == TaskMode.translate_to_string(TaskMode.NUT)):
                return [task_one, task_two]
            else:
                if (task_one.pre_conditions is None) and (task_two.pre_conditions is None):
                    return [task_one, task_two]
                elif (task_one.pre_conditions is None) and (task_two.pre_conditions is not None):
                    return [task_one, task_two]
                elif (task_one.pre_conditions is not None) and (task_two.pre_conditions is None):
                    condition = all(
                        flag.task_id == task_two.task_id for flag in task_one.pre_conditions)
                    if condition:
                        return [task_two, task_one]
                    return [task_one, task_two]
                else:
                    condition_one = all(
                        flag.task_id == task_one.task_id for flag in task_two.pre_conditions)
                    condition_two = all(
                        flag.task_id == task_two.task_id for flag in task_one.pre_conditions)

                    if condition_one and condition_two:
                        return [task_one, task_two]
                    elif condition_one:
                        return [task_one, task_two]
                    elif condition_two:
                        return [task_two, task_one]
                    return [task_one, task_two]

        else:
            if task_one.mode == TaskMode.translate_to_string(TaskMode.VUT):
                return [task_one, task_two]
            elif task_one.mode == TaskMode.translate_to_string(TaskMode.SEQ):
                if task_two.mode == TaskMode.translate_to_string(TaskMode.VUT):
                    return [task_two, task_one]
                return [task_one, task_two]
            else:
                return [task_two, task_one]

    def order_task(self, task_data: list):
        # task_data = [TakeOffTask, GoToTask, WaitTask, LandTask]

        n = len(task_data)
        for i in range(n):

            already_sorted = True

            for j in range(n - i - 1):
                order = self.__compare_task(
                    self, task_data[j], task_data[j + 1])
                task_data[j], task_data[j + 1] = order[0], order[1]

                already_sorted = False

            if already_sorted:
                break

        return task_data

    def insert_task(self, task_data: list, new_task):
        task_data.append(new_task)
        return self.order_task(self, task_data)

    def remove_task(self, task_data: list, remove_task):
        for task in task_data:
            if task.pre_conditions is not None:
                for pre_condition in task.pre_conditions:
                    if pre_condition.task_id == remove_task.task_id:
                        self.remove_task(self, task_data, task)

        task_data.remove(remove_task)
