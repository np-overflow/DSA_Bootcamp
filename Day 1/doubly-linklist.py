class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def print_list(self):
         temp = self.head
         for i in range(self.length):
               print(temp.value)
               temp = temp.next

         return 

    def append(self, value):
        node = Node(value)
        temp = self.head
        for i in range(self.length -1):
            temp = temp.next
        temp.next = node
        node.prev = temp
        self.length +=1
        

    def insert(self, index, value):
         if (index > (self.length) or index < 0):
              return False
         else:
              node = Node(value)
              if index == 0:
                   node.next = self.head
                   self.head.prev = node
                   self.head = node
              else:
                    temp = self.head
                    for i in range(index-1):
                         temp = temp.next
                    
                    node.prev = temp
                    node.next = temp.next
                    temp.next = node
          

              self.length +=1

              return True

    def remove(self, index):
         if (index < 0 or index > self.length -1):
              return False
         
         else:
               if (index ==0):
                temp = self.head.next
                self.head = None
                self.head = temp
               else:
                temp = self.head
                for i in range(index -1):
                    temp = temp.next

                if index ==self.length -1:
                    
                    temp.next = None
                else:
                    temp2 = temp.next
                    temp.next = temp2.next
                    temp.next.prev = temp
                    temp2 = None
              
              
               self.length -=1

    def search(self, target):
          temp = self.head
          for x in range(self.length):
                 if temp.value == target:
                      return True
                 temp = temp.next
          return False


doubly = DoublyLinkedList(10)
doubly.append(8)
doubly.append(28)
doubly.insert(0, 6)
doubly.print_list()
print(doubly.search(4))
print()
doubly.remove(3)
doubly.print_list()
