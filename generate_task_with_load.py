import random
import string
import sys
import csv
import math

argv = sys.argv
load = argv[1]
current_load = 0
with open('tasks.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    while True:
        # generate random string task name
        name = 'task_' + \
            ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        # generate random execution time
        execution_time = random.randint(5, 10)
        runtime = execution_time + 1  # assign a runtime slightly larger than execution time
        period = random.randint(20, 50)  # generate period
        if current_load + execution_time / period >= int(load) / 100:
            period = math.floor(
                execution_time / (int(load) / 100 - current_load))
            writer.writerow([name, execution_time, runtime, period])
            break
        else:
            current_load += execution_time / period
            writer.writerow([name, execution_time, runtime, period])
csvFile.close()
