class QueueError(IndexError): 
    pass


class Queue:
    def __init__(self):
        self.__queue = []
        

    def put(self, elem):
        self.__queue.insert(0,elem)

    def get(self):
        try:
           return self.__queue.pop()
        except:
            raise QueueError
    def __str__(self):
        return ', '.join([str(elem) for elem in self.__queue])

class SuperQueue(Queue):
    def __init__(self):
        super().__init__()
        
    def isempty(self):
        return not self._queue
