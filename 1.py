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

   def deleteN(self, k):
       p1 = p2 = self.head

       if k > self.size:
           print("size error")
           return 0
       elif k is self.size:
           k -= 1
           if k != 0:
               for i in range(k):
                   p2 = p2.next
               if p2 is None:
                   return None
           while p2.next is not None:
               p2 = p2.next
               p1 = p1.next
           self.head = p1.next
       else:
           if k != 0:
               for i in range(k):
                   p2 = p2.next
               if p2 is None:
                   return None
           while p2.next is not None:
               p2 = p2.next
               p1 = p1.next
           p1.next = p1.next.next


if __name__ == '__main__':
   node = LinkedList()
   node.append(1)
   node.append(2)
   node.append(3)
   node.append(4)
   node.append(5)
   node.print_list()
   print("N =", 2)
   node.deleteN(2)
   node.print_list()
   print("------------------------------")

   node2 = LinkedList()
   node2.append(1)
   node2.append(2)
   node2.append(3)
   node2.print_list()
   print("N =", 3)
   node2.deleteN(3)
   node2.print_list()
   print("------------------------------")

   node3 = LinkedList()
   node3.append(1)
   node3.print_list()
   print("N =", 1)
   node3.deleteN(1)
   node3.print_list()