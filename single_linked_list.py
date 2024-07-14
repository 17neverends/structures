class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SinlgeLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert_at_start(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def delete(self, value):
        current_node = self.head

        if current_node and current_node.value == value:
            self.head = current_node.next
            current_node = None
            return
        prev_node = None
        while current_node and current_node.value != value:
            prev_node = current_node
            current_node = current_node.next
        if current_node is None:
            return
        prev_node.next = current_node.next
        current_node = None

    def find(self, value) -> bool:
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return True
            current_node = current_node.next
        return False

    def display(self) -> None:
        current_node = self.head
        while current_node:
            print(current_node.data + ' -> ')
            current_node = current_node.next
        print("None")
