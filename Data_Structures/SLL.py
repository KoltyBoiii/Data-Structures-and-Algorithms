class SLLNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __str__(self):
        value_list = []
        temp = self.head

        if temp is None:
            return str(value_list)
        
        while temp:
            value_list.append(temp.value)
            temp = temp.next

        return str(value_list)

    def get_size(self):
        return self.size
    
    def is_empty(self):
        if self.size == 0:
            return True
        return False
    
    def add_first(self, value):
        temp = self.head
        self.head = SLLNode(value)
        self.head.next = temp
        self.size += 1
        return
    
    def add_last(self, value):
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = SLLNode(value)
        self.size += 1
        return
    
    def remove_first(self):
        if self.head is None:
            return 
        node_value = self.head.value
        self.head = self.head.next
        return node_value
        
    def remove_last(self):
        temp = self.head
        if temp is None:
            return
        while temp.next.next:
            temp = temp.next
        
        node_value = temp.next.value
        temp.next = temp.next.next
        return node_value

    def min(self):
        if self.head == None:
            return None
        if self.head.next == None:
            return self.head.value
        
        min_value = self.head.value
        temp = self.head
        while temp.next:
            if temp.next.value < min_value:
                min_value = temp.next.value
            temp = temp.next
            
        return min_value
    
    def get(self, index):
        temp = self.head
        if temp is None:
            return
        if index >= self.size:
            raise IndexError
        for i in range(index):
            temp = temp.next
        recieved_value = temp.value
        return recieved_value

    def remove_at_index(self, index: int):
        temp = self.head
        if temp is None:
            return
        
        if index >= self.size:
            raise IndexError
        
        for i in range(index - 1):
            temp = temp.next
        
        del_node_value = temp.next.value
        temp.next = temp.next.next

        return del_node_value
sll = SinglyLinkedList()
sll.add_first(1)
sll.add_first(2)
sll.add_first(3)
sll.add_first(4)
sll.add_first(5)
print(sll.get(2))
print(sll)