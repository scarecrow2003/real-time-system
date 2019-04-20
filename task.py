import simpy


class Task(object):
    def __init__(self, env, name, execution_time, runtime, period):
        self.env = env
        self.name = name
        self.execution_time = execution_time
        self.remaining_execution_time = execution_time
        self.runtime = runtime
        self.period = period
        self.remaining_runtime = runtime
        self.deadline = period
        self.next_deliver_time = period

