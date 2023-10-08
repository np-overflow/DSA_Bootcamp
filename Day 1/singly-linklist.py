class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.length = 1

    # APPEND
    def append(self, value):
        node = Node(value)
        if self.head!= None:
            temp = self.head
            for i in range(self.length -1):
                temp = temp.next
            temp.next = node
        else:
            self.head = node
        self.length +=1


    # INSERT
    def insert(self, index, value):
         if (index > (self.length) or index < 0):
              return False
         else:
              node = Node(value)
              if index == 0:
                   node.next = self.head
                   self.head = node
              else:
                    temp = self.head
                    for i in range(index-1):
                         temp = temp.next
                    
                    node.next = temp.next
                    temp.next = node
          

              self.length +=1

              return True

    # REMOVE
    def remove(self, index):
             if (index < 0 or index > self.length -1):
              return False
             else:
               if (index == 0):
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
                    temp2 = None
              
               self.length -=1
               return True

    def search(self, target):
          temp = self.head
          for x in range(self.length):
                 if temp.value == target:
                      return True
                 temp = temp.next
          return False

    def print_list(self):
       if self.length != 0:
            temp = self.head
            for i in range(self.length):
                    print(temp.value)
                    temp = temp.next

            return 
       else:
            print("Empty List!")


singly = SinglyLinkedList(10)
singly.remove(0)
singly.print_list()
singly.insert(0,8)
singly.append(28)
singly.insert(2, 6)
singly.print_list()
print(singly.search(8))
print()
singly.remove(1)
print(singly.search(8))
singly.print_list()
