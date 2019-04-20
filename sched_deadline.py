import simpy
import csv
import math
from task import Task


def sched_deadline(env, tasks):
    print('start to schedule tasks')
    missed_deadline = 0
    while True:
        current_time = env.now
        print('time now is ', current_time)
        if current_time > 5000:
            total_scheduled = 0
            for name, task in tasks.items():
                total_scheduled += math.floor(5000 / task.period)
            print('percentage of missed deadline: ', missed_deadline * 100 / total_scheduled, '%')
            break
        for name, task in tasks.items():
            if task.next_deliver_time < current_time:
                if task.remaining_execution_time > 0:
                    missed_deadline += 1
                    print('missed deadline: ', str(missed_deadline))
                task.remaining_execution_time += task.execution_time
                task.next_deliver_time += task.period

            need_reset = False
            if task.deadline <= current_time:
                need_reset = True
            elif (task.deadline - current_time) * task.runtime / task.period < task.remaining_runtime:
                need_reset = True
            if need_reset:
                task.deadline = current_time + task.period
                task.remaining_runtime = task.runtime
        selected_task = get_earliest_deadline_task(tasks)
        if selected_task is None:
            print('no task is ready')
            yield env.timeout(1)
        else:
            print(selected_task.name, ' with deadline ',
                  selected_task.deadline, ' is selected to run')
            yield env.process(run_task(selected_task))


def run_task(task):
    start = task.env.now
    print(task.name, ' starts to run at ', start)
    time_to_run = 1
    yield task.env.timeout(time_to_run)
    task.remaining_runtime -= time_to_run
    task.remaining_execution_time -= time_to_run


def get_earliest_deadline_task(tasks):
    earliest_deadline_task = None
    for name, task in tasks.items():
        if earliest_deadline_task is None:
            if (task.remaining_execution_time > 0) & (task.remaining_runtime > 0):
                earliest_deadline_task = task
        elif (task.deadline < earliest_deadline_task.deadline) & (task.remaining_execution_time > 0) & (task.remaining_runtime > 0):
            earliest_deadline_task = task
    return earliest_deadline_task


tasks = {}
env = simpy.Environment()
with open('tasks.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        tasks[row[0]] = Task(env, row[0], int(
            row[1]), int(row[2]), int(row[3]))

env.process(sched_deadline(env, tasks))
env.run()
