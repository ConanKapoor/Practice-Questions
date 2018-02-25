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

    def Count_Occurence(self,item):
        temp = self.head
        count = 0

        while temp is not None:
            if temp.data == item:
                count += 1
            temp = temp.next

        print "The number of occurence of %s in Linked list is: %s" %(item,count)

if __name__ == '__main__':
    LL = LinkedList()
    LL.add_node(1)
    LL.PrintLL()
    LL.add_node(2)
    LL.PrintLL()
    LL.add_node(2)
    LL.PrintLL()
    LL.add_node(4)
    LL.PrintLL()
    LL.add_node(5)
    LL.PrintLL()
    LL.Count_Occurence(2)
