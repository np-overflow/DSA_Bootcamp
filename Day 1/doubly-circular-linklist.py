import math

def test(n): #space complexity example
    testlist = []
    for i in range(math.ceil(math.log(n))):
        testlist.append(i)



class Node:
    def __init__(self, data):
        self.value = data
        self.next: Node = None
        self.prev :Node = None

class CircularLinkedList:
    def __init__(self,data):
        node = Node(data)
        self.head = node
        self.length = 1
        self.head.prev = self.head
        self.head.next = self.head
    
    def append(self,data):
            node = Node(data)
            if self.length != 0:
                    temp = self.head.prev
                    temp.next = node
                    node.next = self.head
                    node.prev = temp
                    self.head.prev = node 
                    self.length+= 1
                    return
            else:
                self.head = node
                self.head.prev = self.head
                self.head.next = self.head
                self.length+= 1
                return

    def insert(self,index:int,data):
         if (index > (self.length) or index < 0):
              return False
         else:
              node = Node(data)
              if index == 0:
                   node.prev = self.head.prev
                   self.head.prev.next = node
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
                    
                    if (index == self.length):
                         self.head.prev = node
                         node.next == self.head
          

              self.length +=1

              return True
              
    def search(self, target):
            temp = self.head
            for i in range(self.length):
                 if temp.value == target:
                      return True
                 temp = temp.next
            return False

    def print_list(self):
          temp = self.head
          for i in range(self.length):
               print(temp.value)
               temp = temp.next

          return 
              
    
    def remove(self,index:int):
         if (index < 0 or index > self.length -1):
              return False
         else:
               if (index ==0):
                temp = self.head.next
                temp.prev = self.head.prev
                self.head.prev.next = temp
                self.head = None
                self.head = temp
               else:
                temp = self.head
                for i in range(index -1):
                    temp = temp.next
                
                temp2 = temp.next
                temp.next = temp2.next
                temp.next.prev = temp
                temp2 = None
              
               self.length -=1
               return True


if __name__ == "__main__":
    doubly = CircularLinkedList(11)
    doubly.append(5) 
    doubly.append(6)
    doubly.insert(3,9)
#     doubly.append(7)
#     doubly.append(8)
    doubly.print_list()
    print(doubly.search(11))
    doubly.remove(1)
    print()
    doubly.print_list()
    test(5)