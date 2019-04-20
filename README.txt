1. Install package simpy by running `pip install simpy`

2. Generate task use `python generate_task_with_load.py <load_percentage>`. Use a number of percentage to
replace <load_percentage>, e.g. 80, 90, etc. The generate task set will be stored in file tasks.csv

3. Use `python sched_deadline.py` to schedule the generated tasks using SCHED_DEADLINE. The scheduler will
 run until time reaches 5000. The result of percentage of missed deadline will be printed out at the end
 of the program.

4. Use `python sched_fifo.py` to schedule the generated tasks using SCHED_FIFO. The scheduler will run
until time reaches 5000. The result of percentage of missed deadline will be printed out at the end of
the program.

5. The outcome of two algorithm can be compared.

6. Repeat 2 to 5 for different load percentage and compare the result.