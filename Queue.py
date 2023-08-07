class Queue:        # Queue Class
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        if self.__len__() == 0:
            return True
        else:
            return False

    def __len__(self):
        return len(self.queue)
    
    def enqueue(self, item):    # Add items to queue 
        self.queue.append(item)

    def dequeue(self):      # Remove and return first item in list/queue (position 0)
        assert not self.isEmpty(), "Cannot deque from an empty queue"
        return self.queue.pop(0)

class MemRequest:
    def __init__(self, mem_id, req):
        self.__memID =  mem_id
        self.__request = req

    def getMemID(self):
        return self.__memID
    
    def getRequest(self):
        return self.__request 
