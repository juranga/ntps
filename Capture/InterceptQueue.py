import queue
from queue import * 

class InterceptQueue(Queue):

    def __init__(self, size=100):
        self.queue = Queue(size)
        self.size

    def change_queue_size(self):
        #TODO: Code to populate new queue with old queue, but larger size.
        return self.size

