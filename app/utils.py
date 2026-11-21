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


def calculate_total(prices : list[float]) ->float:
    return sum(prices)


def get_discount(total:float, percentage:float)->float:
    discount_amount = total * (percentage/100)
    return total - discount_amount

def create_order(order_id:int, items:list[str],total:float)->dict:
    return {
        "order" : order_id,
        "name" : items,
        "total" : total
    }