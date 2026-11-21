def calculate_avg(values:list[float]) -> float:
    return sum(values)/len(values)


def create_task(task_id:int, task_name:str)->dict:
    return  {
        "id" : task_id,
        "name" : task_name,
        "completed": False
    }


def format_task(task:dict)->str:
    return f"Task {task['id']}: {task['name']}"