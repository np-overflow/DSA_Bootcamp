import math

def test(n): #space complexity example
    testlist = []
    for i in range(math.ceil(math.log(n))):
        testlist.append(i)



class Node:
    def __init__(self, data):
        self.data = data
        self.next: Node = None
        self.previous :Node = None

class circular_linkedList:
    def __init__(self):
        self.head: Node = None
        self.size = 0
    
    def _append(self,data):
            node = Node(data)
            if self.head != None:
                    temp = self.head.previous
                    temp.next = node
                    node.next = self.head
                    node.previous = temp
                    self.head.previous = node 
                    self.size+= 1
                    return
            else:
                self.head = node
                self.head.previous = self.head
                self.head.next = self.head
                self.size+= 1
                return

    def _insertAt(self,index:int,data):
         if (index > (self.size) or index < 0):
              return False
         else:
              node = Node(data)
              temp = self.head
              for i in range(index-1):
                   temp = temp.next
            
              node.previous = temp
              node.next = temp.next
              temp.next = node
              return
              
    def _search(self, target):
            temp = self.head
            while (True):
                if target == temp.data:
                    return True
                temp = temp.next
                if temp == self.head:
                    return False

    def _print(self):
         temp = self.head
         while (True):
              print(temp.data)
              temp = temp.next
              if (temp == self.head):
                  return
              
    def _dequeue(self):
         temp = self.head.previous
         if self.size == 1:
              self.head = None
         else:
               beforeTemp = temp.previous
               beforeTemp.next = self.head
               self.head.previous =beforeTemp
               temp = None
    
    def _deleteAt(self,index:int):
         if (index < 0 or index > self.size -1):
              return False
         else:
              if self.size == 1:
                   self.head =None
              else:  
               if (index ==0):
                temp = self.head.next
                temp.previous = self.head.previous
                self.head.previous.next = temp
                self.head = None
                self.head = temp
               else:
                temp = self.head
                for i in range(index -1):
                    temp = temp.next
                temp.next = temp.next.next
                temp.next.previous = temp
                temp = None


if __name__ == "__main__":
    doubly = circular_linkedList()
    doubly._append(5) 
    doubly._append(6)
    doubly._insertAt(1,9)
    doubly._append(7)
    doubly._append(8)
    doubly._deleteAt(2)
    print(doubly._search(20))
    doubly._print()
    test(5)