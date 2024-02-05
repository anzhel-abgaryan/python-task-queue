from flask import Flask, request
import threading
import time

from classes import TaskQueue, Resources, Task
from constants import CPU_CORES, GPU_COUNT, RAM

available_resources = Resources(cpu_cores=CPU_CORES,
                                gpu_count=GPU_COUNT,
                                ram=RAM)

queue = TaskQueue()
app = Flask(__name__)


@app.route("/", methods=["POST"])
def task_handler():
    queue.add_task(request.json)
    queue.print_queue()

    return "Success!"


def consumer():
    while True:
        task = queue.get_task(available_resources)
        if isinstance(task, Task):
            print(f"Top priority task with available resources for thread {threading.current_thread().name}: {task}",
                  '\n')

            available_resources.cpu_cores -= task.resources['cpu_cores']
            available_resources.ram -= task.resources['ram']
            available_resources.gpu_count -= task.resources['gpu_count']
            time.sleep(2)
            available_resources.cpu_cores += task.resources['cpu_cores']
            available_resources.ram += task.resources['ram']
            available_resources.gpu_count += task.resources['gpu_count']
        else:
            time.sleep(2)
            print(f"{threading.current_thread().name} {task}", "\n")


if __name__ == '__main__':
    get_thread = threading.Thread(target=consumer)
    get_thread.start()

    app.run(port=8080)
    get_thread.join()
