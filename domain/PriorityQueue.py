"""
The priority queue Class which will help us in the Dijkstra's Algorithm and Prim's Algorithm implementation
"""


class PriorityQueue:
    def __init__(self):
        self.__values = {}

    def is_empty(self):
        return len(self.__values) == 0

    def pop(self):
        top_priority = None
        top_object = None
        for obj in self.__values:
            obj_priority = self.__values[obj]
            if top_priority is None or top_priority > obj_priority:
                top_priority = obj_priority
                top_object = obj
        del self.__values[top_object]
        return top_object

    def add(self, obj, priority):
        self.__values[obj] = priority

    def contains(self, val):
        return val in self.__values


