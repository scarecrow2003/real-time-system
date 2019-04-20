import simpy
import csv
import math
from queue import Queue
from task import Task


def sched_fifo(env, tasks):
    print('start to schedule tasks')
    missed_deadline = 0
    queue = Queue()
    current_task = None
    while True:
        current_time = env.now
        print('time now is ', current_time)
        if current_time == 80:
            print('80')
        if current_time > 5000:
            total_scheduled = 0
            for name, task in tasks.items():
                total_scheduled += math.floor(5000 / task.period)
            print('percentage of missed deadline: ', (missed_deadline + queue.qsize()) * 100 / total_scheduled, '%')
            break
        for name, task in tasks.items():
            if current_time % task.period == 0:
                queue.put(TaskWrapper(task, task.remaining_execution_time, current_time + task.period))
        if (current_task is None) & (not queue.empty()):
            current_task = queue.get()
        if current_task is not None:
            yield env.process(run_task(current_task))
            if current_task.remaining_execution_time == 0:
                time = env.now
                if time > current_task.abs_deadline:
                    missed_deadline += 1
                    print('missed deadline: ', str(missed_deadline))
                current_task = None
        else:
            yield env.timeout(1)


def run_task(task):
    start = task.task.env.now
    print(task.task.name, ' starts to run at ', start)
    time_to_run = 1
    yield task.task.env.timeout(time_to_run)
    task.remaining_execution_time -= time_to_run


class TaskWrapper(object):
    def __init__(self, task, remaining_execution_time, abs_deadline):
        self.task = task
        self.remaining_execution_time = remaining_execution_time
        self.abs_deadline = abs_deadline


tasks = {}
env = simpy.Environment()
with open('tasks.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        tasks[row[0]] = Task(env, row[0], int(
            row[1]), int(row[2]), int(row[3]))

env.process(sched_fifo(env, tasks))
env.run()
