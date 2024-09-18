# class Stack:
#     def __init__(self):
#         self.__stackList = []
#
#     def push(self, val):
#         self.__stackList.append(val)
#         return self.__stackList
#
#     def pop(self):
#         val = self.__stackList[-1]
#         del self.__stackList[-1]
#         return val
#
#
# class AddingStack(Stack):
#     def __init__(self):
#         Stack.__init__(self)
#         self.__sum = 0
#
#     def push(self, parentlist):
#         for i in parentlist:
#             self.__sum += i
#         return self.__sum
#
#
# obj = Stack()
# mylist = obj.push(3)
# mylist = obj.push(2)
# mylist = obj.push(1)
#
# obj2 = AddingStack()
# print(obj2.push(mylist))


# # Task 1 (Stack)
# class Stack:
#     def __init__(self):
#         self.__stk = []
#
#     def push(self, val):
#         self.__stk.append(val)
#
#     def pop(self):
#         val = self.__stk[-1]
#         del self.__stk[-1]
#         return val
#
#
# class CountingStack(Stack):
#     def __init__(self):
#         super().__init__()
#         self.__count = 0
#
#     def get_counter(self):
#         return self.__count
#
#     def pop(self):
#         self.__count += 1
#
#
# #
# # Do pop and update the counter.
# #
#
#
# stk = CountingStack()
# for i in range(100):
#     stk.push(i)
#     stk.pop()
# print(stk.get_counter())


# Queue Task
# class QueueError(Exception):  # Choose base class for the new exception.
#     """There is an error with the Queue."""
#
#
# class Queue:
#     def __init__(self):
#         self.__queue = []
#
#     def put(self, elem):
#         self.__queue.append(elem)
#
#     def get(self):
#         if len(self.__queue) == 0:
#             raise QueueError("Queue is empty")  # Raise the custom exception with a message
#         return self.__queue.pop(0)  # Use pop(0) to get the first element from the queue
#
#
# que = Queue()
# que.put(1)
# que.put("dog")
# que.put(False)
#
# try:
#     for i in range(4):  # Trying to get more elements than are in the queue
#         print(que.get())
# except QueueError as e:
#     print(f"Queue error: {e}")

# Queue Task 3.2.1.16 FIFO

class QueueError(Exception):  # Choose base class for the new exception.
    pass


class Queue:
    def __init__(self):
        self.__queue = []

    def put(self, elem):
        self.__queue.append(elem)

    def get(self):
        if len(self.__queue) == 0:
            raise QueueError  # Raise the custom exception with a message
        return self.__queue.pop(0)  # Use pop(0) to get the first element from the queue

class SuperQueue(Queue):
    def isempty(self):
        return len(self._Queue__queue) == 0


que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")


