from typing import List, Dict, Union
from dataclasses import dataclass


@dataclass
class Resources:
    ram: int
    cpu_cores: int
    gpu_count: int


@dataclass
class Task:
    id: int
    priority: int
    resources: Resources
    content: str
    result: str


class TaskQueue:
    queue: List[Task] = []

    def add_task(self, request: Dict[str, Union[str, int]]):
        task = Task(id=request['id'],
                    priority=request["priority"],
                    resources=request["resources"],
                    content=request["content"],
                    result=request["result"]
                    )

        self.queue.append(task)

    def get_task(self, available_resources: Resources) -> Union[str, Task]:
        if len(self.queue) > 0:
            self.queue.sort(key=lambda x: x.priority)
            queue_len = len(self.queue)

            for i in range(1, queue_len + 1):
                top_task = self.queue[queue_len - i]
                if available_resources.ram >= top_task.resources['ram'] and \
                        available_resources.cpu_cores >= top_task.resources['cpu_cores'] and \
                        available_resources.gpu_count >= top_task.resources['gpu_count']:
                    top_task = self.queue.pop(queue_len - i)
                    return top_task
            return f"No available resource for any task, current resources: {available_resources}"

        return "The queue is empty."

    def sort_queue(self):
        while True:
            if len(self.queue) > 0:
                self.queue.sort(key=lambda x: x.priority)

    def print_queue(self):
        print(self.queue)


