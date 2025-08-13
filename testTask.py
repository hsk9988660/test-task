import time

class Task:
    def __init__(self, id, processing_time, waiting_time, user_tier):
        self.id = id
        self.processing_time = processing_time 
        self.waiting_time = waiting_time        
        self.user_tier = user_tier

    def calculate_priority(self):
        """
        Lower value = higher priority.
        Paid users get higher priority than Free users.
        Waiting time and processing time also affect priority.
        """
        user_priority = 1 if self.user_tier == 'Paid' else 2
        return (user_priority * 1000000) + self.waiting_time + self.processing_time

    def __repr__(self):
        return f"Task({self.id}, {self.user_tier}, Wait:{self.waiting_time}, Proc:{self.processing_time})"


class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, task):
        self.queue.append(task)
        self.sort_queue()

    def sort_queue(self):
        self.queue.sort(key=lambda x: x.calculate_priority())

    def process_task(self):
        if self.is_empty():
            return None

        task = self.queue.pop(0)
        print(f"\nProcessing Task {task.id} (User: {task.user_tier}, Waited: {task.waiting_time}ms, Time: {task.processing_time}ms)")

        # Simulate actual task processing time
        time.sleep(task.processing_time / 1000)  # convert ms -> seconds

        for t in self.queue:
            t.waiting_time += task.processing_time

        self.sort_queue()

        print("Queue after processing:", self.queue)
        return task

    def is_empty(self):
        return len(self.queue) == 0


task_queue = PriorityQueue()

# Enqueue tasks
task_queue.enqueue(Task(1, 2000, 1000, 'Free'))
task_queue.enqueue(Task(2, 1500, 3000, 'Paid'))
task_queue.enqueue(Task(3, 1000, 1000, 'Free'))
task_queue.enqueue(Task(4, 1000, 1500, 'Paid'))

# Process all tasks
while not task_queue.is_empty():
    task_queue.process_task()
