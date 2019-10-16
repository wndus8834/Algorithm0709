class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

        self.size += 1

    def print_list(self):
        p = self.head
        if p is not None:
            while p:
                if p.next is not None:
                    print(p.data, '-> ', end='')
                else:
                    print(p.data)
                p = p.next
        else:
            print("null")

    def mergeSorted(self, list1, list2):
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        if list1.data < list2.data:
            temp = list1
            temp.next = self.mergeSorted(list1.next, list2)
        else:
            temp = list2
            temp.next = self.mergeSorted(list1, list2.next)
        return temp


if __name__ == '__main__':
    node = LinkedList()
    node.append(1)
    node.append(2)
    node.append(3)
    node.print_list()

    node2 = LinkedList()
    node2.append(1)
    node2.append(2)
    node2.append(3)
    node2.print_list()

    node3 = LinkedList()
    node3.head = node3.mergeSorted(node.head, node2.head)
    node3.print_list()
    print("------------------------------")

    node4 = LinkedList()
    node4.append(1)
    node4.append(3)
    node4.append(5)
    node4.append(6)
    node4.print_list()

    node5 = LinkedList()
    node5.append(2)
    node5.append(4)
    node5.print_list()

    node6 = LinkedList()
    node6.head = node6.mergeSorted(node4.head, node5.head)
    node6.print_list()
