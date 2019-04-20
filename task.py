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

    # def run(self, finish):
    #     start = self.env.now()
    #     print(self.name, ' starts to run at', start)
    #     time_to_run = self.remaining_execution_time if self.remaining_runtime >= self.remaining_execution_time else self.remaining_runtime
    #     yield self.env.timeout(time_to_run)
    #     self.remaining_runtime -= time_to_run
    #     self.remaining_execution_time -= time_to_run
    #     if self.remaining_execution_time == 0 & self.env.now() > self.deadline:
    #         print('missed deadline')
    #         finish.fail()
    #     else:
    #         finish.succeed()
