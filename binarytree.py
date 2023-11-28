# Binary Tree and Binary Search Tree by Archie Verma 
# This includes: 
# Building up a Tree (step 1 and 2)
# 1. Defining a Tree
# 2. a. Define an insert function(on both left and right) and b. Add a Node
# 3. Printing all nodes InOrder 
# 4. Printing all nodes PreOrder 
# 5. Printing all nodes PostOrder 

# This code is for binary search tree  => What about Binary Tree?=> Comment oout the insert code 
# 1. Defining a Tree usually talking about a binary search tree(each node must have at most(max) two children)
# A node is a tree, a tree is a node once you define a node you have defined a tree
class Node :
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

# # 2.a. Insert function(on both left and right)
#     def insert(self, data) :
#         # Check is the first node is null if so add data in it
#         if self.data is None :
#             self.data = data
#         # Else if the data is not empty we add left or right child 
#         else :      
#            # We write if condition for adding data in the left side see if left node is less than root node
#            # Also, check if it is None to be able to add
#             if data < self.data :
#                 if self.left is None :
#                     self.left = Node(data)
#                 else : 
#                    # If it is not empty, there is something there so we call a recusive function and insert it there
#                    # That means for the left node that already has a value(not empty) we will insert this new node as its child
#                     self.left.insert(data)
#             # Same thing for right here but if the data is greater than root
#             elif data > self.data :
#                 if self.right is None :
#                     self.right = Node(data)
#                 else :
#                     self.right.insert(data)

# 3. Printing all nodes InOrder - L,  Root, R -> a,b,c
          #   Root-b   #
          #   /   \    #
          #  L-a  R-c  #
# Recursive function, r is root here
def inOrderPrint(r) :
    if r is None:
        return
    else:
        inOrderPrint(r.left)
        print(r.data, end= ' ')
        inOrderPrint(r.right) 


# 4. Printing all nodes PreOrder - Root,  L, R ->b,a,c
          #   Root-b   #
          #   /   \    #
          #  L-a  R-c  #
# Recursive function, r is root here 
def preOrderPrint(r) :
    if r is None:
        return
    else:
        print(r.data, end= ' ')
        preOrderPrint(r.left)
        preOrderPrint(r.right) 


# 4. Printing all nodes PostOrder - L, R, Root ->a,c,b
          #   Root-b   #
          #   /   \    #
          #  L-a  R-c  #
# Recursive function, r is root here 
def postOrderPrint(r) :
    if r is None:
        return
    else:
        postOrderPrint(r.left)
        postOrderPrint(r.right)
        print(r.data, end= ' ')  

# 2.b. Add a Node using insert method
if __name__ == '__main__':

    # To Create a binary tree just use this as input and comment the insert code 
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    # For Binary search tree
    # root = Node('b')
    # root.insert('a')
    # root.insert('c')

    # Another Bigger Example for Binary search tree:
    # root = Node('g')
    # root.insert('c')
    # root.insert('b')
    # root.insert('a')
    # root.insert('e')
    # root.insert('d')
    # root.insert('f')
    # root.insert('i')
    # root.insert('h')
    # root.insert('j')
    # root.insert('k')
    print("Welcome to Tree")

# 3. Printing all nodes InOrder
print("InOrder: ")
inOrderPrint(root)
print(" ")
# 4. Printing all nodes PreOrder
print("PreOrder: ")
preOrderPrint(root)
print(" ")
# 4. Printing all nodes PostOrder
print("PostOrder: ")
postOrderPrint(root)

    
        





    
      
