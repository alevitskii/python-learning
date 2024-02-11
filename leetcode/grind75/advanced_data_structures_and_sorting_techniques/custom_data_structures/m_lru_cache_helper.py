class LinkedListNode:
    def __init__(self, pair):
        self.second = pair[1]
        self.first = pair[0]
        self.pair = pair
        self.next = None
        self.prev = None


class LinkedList:
    # _init__ initialises the linkedL list type object
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # move_to_head will move the given node to head
    def move_to_head(self, node):
        if not node:
            return

        if node.prev:
            node.prev.next = node.next

        if node.next:
            node.next.prev = node.prev

        if node == self.head:
            self.head = self.head.next

        if node == self.tail:
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None

        # Insertion at head
        if not self.head:
            self.tail = node
            self.head = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    # Insert_at_head will insert the given pair at head
    def insert_at_head(self, pair):
        new_node = LinkedListNode(pair)
        if not self.head:
            self.tail = new_node
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.size += 1

    # Insert_at_tail will insert the given pair at tail
    def insert_at_tail(self, pair):
        new_node = LinkedListNode(pair)
        if not self.tail:
            self.tail = new_node
            self.head = new_node
            new_node.next = None
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            new_node.next = None

        self.size += 1

    # remove will remove the given pair from the LinkedList
    def remove(self, pair):
        i = self.get_head()
        while i:
            if i.pair == pair:
                self.remove_node(i)
                return
            i = i.next

    # remove_node will remove the given node from the LinkedList
    def remove_node(self, node):
        if not node:
            return

        if node.prev:
            node.prev.next = node.next

        if node.next:
            node.next.prev = node.prev

        if node == self.head:
            self.head = self.head.next

        if node == self.tail:
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
        self.size = self.size - 1
        del node
        # return node

    # remove_head will remove the head of the linked list
    def remove_head(self):
        return self.remove_node(self.head)

    # remove_tail will remove the tail of the linked list
    def remove_tail(self):
        return self.remove_node(self.tail)

    # get_head will return the head of the linked list
    def get_head(self):
        return self.head


def main() -> None:
    main()


if __name__ == "__main__":
    main()
