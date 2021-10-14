# import asyncio

# async def test():
#     await asyncio.sleep(3)


# asyncio.run(test())

# async def get_chat_id(name):
#     await asyncio.sleep(3)
#     return name


# async def main():
#     a = await get_chat_id("azzeem")
#     print(a)

# if __name__ == "__main__":
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())


# '''
#     {
#         "taskType": "WAIT",
#         "taskMode": "SEQ",
#         "taskId": 2,
#         "preConditions": [
#             {
#                 "preConditionTaskId": 1,
#                 "preConditionTaskStatus": "END"
#             }
#         ],
#         "waitTime": 3.0
#     },
#     '''

from task import GoToTask, TaskPlanner, PreCondition
from task import TaskDecoder as td
import json

json_file = open('task_file/main.json', "r")

json_data = json.loads(json_file.read())

lst = td.get_tasks(td, json_data)

# for i in lst:
#     print(i.task_id)

out = TaskPlanner.order_task(TaskPlanner, lst)

newTask = GoToTask("SEQ", 6, 10, 10, 10, [PreCondition(3, "END")])

inserted = TaskPlanner.insert_task(TaskPlanner, out, newTask)

# removed = TaskPlanner.remove_task(TaskPlanner, out, out[0])

for i in inserted:
    print(i.task_id)
