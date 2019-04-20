# import simpy
#
# def sched_deadline(env, tasks, start_event):
#     print('schedule start', env.now)
#     start_event.succeed()
#     yield env.timeout(10)
#
# def periodic_task_creator(env, name, period, task_duration, activation):
#     while True:
#         print('periodic task \'', name, '\' period', period, 'and duration', task_duration, 'waiting for scheduling')
#         yield activation
#         print(name, ' activated')
#         start = env.now
#         try:
#             yield env.timeout(task_duration)
#         except simpy.Interrupt as i:
#             print(name, ' hold')
#             task_duration = task_duration - env.now + start
#
# def greedy_task_creator(env, name, activation):
#     while True:
#         print('greedy task \'', name, '\' waiting for scheduling')
#         yield activation
#         print(name, ' activated')
#         try:
#             yield env.timeout(10000)
#         except simpy.Interrupt as i:
#             print(name, ' hold')
#
# env = simpy.Environment()
# tasks = {}
# reservation = [[6, 1], [10, 1]]
# start_event = env.event()
# for i in range(2):
#     task_name = 'task %d' % i
#     task = env.process(greedy_task_creator(env, task_name, start_event))
#     tasks[task_name] = (task, reservation[i][0], reservation[i][1])
# periodic_task_name = 'task periodic'
# periodic_task = env.process(periodic_task_creator(env, periodic_task_name, 4, 1, start_event))
# tasks[periodic_task_name] = (periodic_task, 4, 1)
# env.process(sched_deadline(env, tasks, start_event))
# env.run()
