class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class CDLL:
    def __init__(self):
        self.cursor = None
        self.size = 0
    
    def __str__(self):
        value_list = []
        temp = self.cursor
        if self.cursor is None:
            print("a")
            return str(value_list)
        if temp is self.cursor:
            print("b")
            value_list.append(temp.value)
            return str(value_list)
        else:
            print("c")
            while temp is not self.cursor:
                value_list.append(temp.value)
                temp = temp.next
        
        return str(value_list)
    
    def add_after_cursor(self, v):
        if self.cursor is None:
            self.cursor = Node(v)
            self.cursor.next = self.cursor
            self.cursor.prev = self.cursor
        else:
            new_node = Node(v)
            new_node.next = self.cursor.next
            new_node.prev = self.cursor
            self.cursor.next = new_node
            new_node.next.prev = new_node
        self.size += 1

    def add_before_cursor(self, v):
        if self.cursor is None:
            self.cursor = Node(v)
            self.cursor.next = self.cursor
            self.cursor.prev = self.cursor
        else:
            new_node = Node(v)
            new_node.next = self.cursor
            new_node.prev = self.cursor.prev
            self.cursor.prev = new_node
            new_node.prev.next = new_node
        self.size += 1

cdll = CDLL()
cdll.add_after_cursor(0)
print(cdll)
cdll.add_after_cursor(1)
print(cdll)
cdll.add_after_cursor(2)
print(cdll)

