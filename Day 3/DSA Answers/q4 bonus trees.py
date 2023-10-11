'''
Bonus: Working with Trees (8 points)
In day 2, slides 37-43, we have learnt the basics of how a tree should be like. 

Given the tree diagram:
 
class TreeNode:
  def __init__(self, data, left=None, right=None):
    self.data = data
    self.left_child = left
    self.right_child = right

Build a tree based on the class TreeNode. Instantiate the nodes 
according to the class TreeNode will do.
Example of how it should look like (printing the tree out is 
optional, no points awarded for that.)
The diagram here is just to illustrate the idea of how you 
should instantiate the Tree nodes.
You are allowed to search up on this.

Fun fact: this is also known as a binary tree, where one node can have 0-2 children.
    5
   / \
  3   8
 /\   /\
1  4 7  9

'''

class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left_child = left # In day 2, slide 41, a child can only have one parent
        self.right_child = right
# Let's instantiate the nodes.

node1 = TreeNode(1) # child node (1m)
node4 = TreeNode(4) # child node (1m) 
node7 = TreeNode(7) # child node (1m)
node9 = TreeNode(9) # child node (1m)

node3 = TreeNode(3, node1, node4) # parent node (1m)
node8 = TreeNode(8, node7, node9) # parent node (1m)

root = TreeNode(5, node3, node8) # root node (2m)
# LOL this line for root was not easy to see.
