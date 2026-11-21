from app.utils import calculate_avg, create_task,format_task

task = create_task("1", "build python backend")
print(format_task(task))

scores = [10,20,30]
average = calculate_avg(scores)

print("average: ", average)