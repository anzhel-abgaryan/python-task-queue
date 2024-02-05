
# Task queue

## Description:
* Requires a task queue with priorities and resource limits.
* Each task has a priority and the required amount of resources to process it.
* Publishers create tasks with specified resource limits, and put them in a task queue.
* Consumer receives the highest priority task that satisfies available resources.
* The queue is expected to contain thousands of tasks.


## How to run:
* You can either run **main.py** and send POST requests, and use the code,
* Or test with **demonstration.py** file, which already contains a generation of randomized mock data.