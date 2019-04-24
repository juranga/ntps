import queue
from queue import * 

class Intercept_Queue(Queue):

    def __init__(self, size=100):
        self.intercept_queue = Queue(size)
        self.size = size

    def change_queue_size(self, size):
        temp_queue = Queue(size)
        for i in range(0, self.size):
            temp_queue.put(self.intercept_queue.get())
        self.intercept_queue = temp_queue

    def get_size(self):
        return self.size
