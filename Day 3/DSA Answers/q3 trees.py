'''
3.	Working with Trees (8 points)
Given the tree diagram:
 
class TreeNode:
  
  def __init__(self, data, left=None, right=None):
    self.data = data
    self.left_child = left
    self.right_child = right

Build a class for a weighted graph. It should minimally include the functions of adding a vertex (circle) and adding an edge (arrow). 
You are allowed to try instantiating the nodes, as node1, node2, etc.
'''

class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left_child = left
        self.right_child = right


class WeightedGraph:
    def __init__(self):
        self.vertices = {}
  
    def add_vertex(self, vertex):
        # Set the data for the vertex
        self.vertices[vertex] = []
    
    def add_edge(self, source, target, weight):
        # Set the weight
        self.vertices[source].append([target, weight])
