class Node:
    def __init__(self, value, prev_node = None, next_node = None):
        self.value = value
        self.prev = prev_node
        self.next = next_node

    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return self.__str__()
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get_size(self): #works
        return self.size
    
    def is_empty(self): #works
        if self.size == 0:
            return True
        return False
        
    def __str__(self):
        #implement the str method for this class
        value_list = []
        if self.head and self.tail is None:
            return str(value_list)
        else:
            temp = self.head
            while temp:
                value_list.append(temp.value)
                temp = temp.next
        return str(value_list)
    
    def add_first(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            node = Node(value)
            temp = self.head
            node.next = temp
            temp.prev = node
            self.head = node
        self.size += 1
        return
    
    def add_last(self, value):
        if self.size == 0:
            self.tail = Node(value)
            self.head = self.tail
        else:
            node = Node(value)
            temp = self.head
            while temp.next:
                temp = temp.next
            self.tail = node
            node.prev = temp
            temp.next = node
                
        self.size += 1
        return

    def remove_first(self):
        del_value = self.head.value
        if self.head is None:
            return "List is empty"
        if self.head.next is None:
            self.head = None
        else:
            temp = self.head.next
            self.head = None
            self.head = temp
        self.size -= 1
        return del_value

    def remove_last(self):
        del_value = self.tail.value
        if self.tail is None:
            return "List is empty"
        if self.tail.prev is None:
            self.tail = None
        else:
            temp = self.tail.prev
            temp.next = None
            self.tail = temp
        self.size -= 1
        return del_value

    def get(self, index: int):
        if self.head is None or index >= self.size:
            raise IndexError
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        return temp.value

    def remove_at_index(self, index: int):
        if self.head is None or index > self.size:
            raise IndexError
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            if temp.next is None:
                print("A")
                del_value = temp.value
                temp.prev.next = None
            elif temp.prev is None:
                print("b")
                del_value = temp.value
                self.head = None
                self.head = temp.next
            else:
                print('c')
                del_value = temp.value
                temp.next.prev = temp.prev
                temp.prev.next = temp.next
        self.size -= 1
        return del_value

    def search(self, value):
        if self.head is None:
            return "List is empty"
        else:
            temp = self.head
            for i in range(self.size - 1):
                if temp.value == value:
                    return i
                temp = temp.next
        return "not in list"

    def first(self):
        if self.head is None:
            return
        return self.head.value
    
    def last(self):
        if self.tail is None:
            return
        return self.tail.value
node_list = DoublyLinkedList()
for i in range(10):
    node_list.add_first(i)

# def dll_tester():
#     # create a DoublyLinkedList
#     test_list = DoublyLinkedList()
    
#     #testing list creation
#     assert test_list.get_size()==0,   'list should be empty to start!'
    
#     #testing add_first
#     test_list.add_first(1)
#     assert test_list.first() == 1, 'add_first needs adjustment!'
#     assert test_list.last() == 1, 'add_first needs adjustment!'
#     assert test_list.get_size() == 1 ,    'add_first needs adjustment!'
#     test_list.add_first(2)
#     assert test_list.first() == 2, 'add_first needs adjustment!'
#     assert test_list.last() == 1, 'add_first needs adjustment!'
#     assert test_list.get_size() == 2, 'add_first needs adjustment!'
    
#     #testing add_last
#     test_list.add_last(3)
#     assert test_list.first() == 2,'add_last needs adjustment!'
#     assert test_list.last() == 3, 'add_last needs adjustment!'
#     assert test_list.get_size() == 3, 'add_last needs adjustment!'

#     #test remove_first
#     assert test_list.remove_first() == 2, 'remove_first needs adjustment!'
#     assert test_list.first() == 1, 'remove_first needs adjustment!'
#     assert test_list.last() == 3, 'remove_first needs adjustment!'
#     assert test_list.get_size() == 2, 'remove_first needs adjustment!'

#     #test remove_last
#     assert test_list.remove_last() == 3, 'remove_last needs adjustment!'
#     assert test_list.first() == 1, 'remove_last needs adjustment!'
#     assert test_list.last() == 1, 'remove_last needs adjustment!'
#     assert test_list.get_size() == 1, 'remove_last needs adjustment!'

#     while not test_list.is_empty():
#         test_list.remove_first()

#     assert test_list.get_size() == 0, 'list should be empty after removing all values'    
#     for i in range(10):
#         test_list.add_last(i+1)
#     #test get method
#     assert test_list.get(0) == 1, 'get(0) should return the element at first index'
#     assert test_list.get(5) == 6, 'get(1) should return the element at index 1'
#     assert test_list.get(9) == 10, 'get(9) should return the element at last index'

#     print('All tests passed!')

# dll_tester()