from src import TaskDecoder, TaskType, TakeOffTask

models = TaskDecoder().get_tasks()
print(len(models))

if type(models[0]) == TakeOffTask:
    task = models[0]
    print(task.height)
# print(TaskType.translate_from_string("LAND"))
