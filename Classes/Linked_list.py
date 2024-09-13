class Linked_list:
    def __init__(self):
        pass

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def add_next(self, Node):
        self.next = Node

    def get_next(self):
        return self.next
    
    def get_data(self):
        return self.data