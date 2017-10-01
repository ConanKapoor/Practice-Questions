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

    def LL_length(self):
        count = 0
        temp = self.head

        while(temp):
            count +=1
            temp = temp.next

        print count

    def templar(self,temp):
        if temp is None:
            return 0
        else:
            return 1 + self.templar(temp.next)

    def LL_length_recursive(self):
        return self.templar(self.head)


if __name__ == '__main__':
    LL = LinkedList()
    LL.add_node(1)
    LL.add_node(2)
    LL.add_node(3)
    LL.LL_length()
    count = LL.LL_length_recursive()
    print count
