class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next
    
class SLL:
    def __init__(self):
        self.head = None

Listy = SLL()

for i in range(4, 0, -1):
    Listy.head = Node(i, Listy.head)

print(Listy.head.data)
print(Listy.head.next.data)
print(Listy.head.next == Listy.head)


# Listy.head = Node(3, None)
# Listy.head = Node(2, Listy.head)
# Listy.head = Node(1, Listy.head)

# temp_node_ref = Node(1, None)

# Listy.head = Node(1, None)
# print(Listy.head.data)

# Listy.head.next = Node(2, None)
# print(Listy.head.next.data)


class Person:
    def __init__(self, name, mom, cat):
        self.name = name
        self.mom = mom
        self.cat = cat

class Cat:
    def __init__(self, name, mom):
        self.name = name
        self.mom = mom

# class SLL:
#     def __init__(self):
#         self.head = None

# Listy = SLL()
# Listy.head = Person("John", None, Cat("Perez", None))

John = Person("John", None, Cat("Perez", None))
John.mom = Person("Marie", None, None)

print(John.mom.cat == John.cat)
John.mom.cat = John.cat
print(John.mom.cat == John.cat)
