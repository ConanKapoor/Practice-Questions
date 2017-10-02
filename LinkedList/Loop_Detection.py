class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None

    def add_node(self,data):
        new_node = Node(data)
        temp = self.head

        if temp is None:
            self.head = new_node
            return

        while(temp.next):
            temp = temp.next

        temp.next = new_node

    def PrintLL(self):
        temp = self.head
        print "Linked list -> "
        while(temp):
            print temp.data,
            temp = temp.next
        print "\n"

    def detect_loop(self):
        self.slow = self.head
        self.fast = self.head
        while (self.slow and self.fast and self.fast.next):
            self.slow = self.slow.next
            self.fast = self.fast.next.next

            if self.slow == self.fast:
                print "Found a loop."
                return

        print "No loop found."

if __name__ == '__main__':
    LL = LinkedList()
    LL.add_node(1)
    LL.PrintLL()
    LL.add_node(2)
    LL.PrintLL()
    LL.add_node(3)
    LL.PrintLL()
    LL.add_node(4)
    LL.PrintLL()
    LL.add_node(5)
    LL.PrintLL()

    # Adding just to detect a loop.
    LL.head.next.next.next.next.next = LL.head
    LL.detect_loop()
