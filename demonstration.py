from numpy.random import randint
from main import consumer
import threading

from classes import Resources, TaskQueue
from constants import CPU_CORES, GPU_COUNT, RAM

available_resources = Resources(cpu_cores=CPU_CORES,
                                gpu_count=GPU_COUNT,
                                ram=RAM)
if __name__ == '__main__':
    queue = TaskQueue()

    for i in range(1000):
        queue.add_task({
            "id": i,
            "priority": randint(100),
            "resources": {

                "ram": randint(16 * 1024),
                "cpu_cores": randint(8),
                "gpu_count": randint(8)
            },
            "content": "some content",
            "result": "some result"
        })

    print("The queue is the following:")
    queue.print_queue()
    print("*" * 100, "\n")

    get_thread = threading.Thread(target=consumer)
    get_thread_1 = threading.Thread(target=consumer)
    get_thread_2 = threading.Thread(target=consumer)

    get_thread.start()
    get_thread_1.start()
    get_thread_2.start()

    get_thread.join()
    get_thread_1.join()
    get_thread_2.join()
