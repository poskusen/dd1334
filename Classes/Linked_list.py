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
    
    def leads_to_end(self, end_node):
        max_iteration = 1000
        iterations = 0
        node = self.get_next()
        while node is not end_node and iterations < 1000:
            iterations += 1
        else:
            return True
        return False