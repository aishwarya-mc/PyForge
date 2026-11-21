from app.utils import calculate_avg, create_task,format_task
from app.utils import calculate_total,get_discount,create_order

task = create_task("1", "build python backend")
print(format_task(task))

scores = [10,20,30]
average = calculate_avg(scores)

print("average: ", average)

prices = [100.0,234.0,567.0]
items = ["keychain","jacket","skirt"]

total = calculate_total(prices)
final_total = get_discount(total, 10.0)
order = create_order(101,items,final_total)
print("order details: ")
print(order)
print("original total: ", total)
print("final total:", final_total)