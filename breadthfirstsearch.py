# Breadth First Search (BFS) using while loop, Python Code - Algorithm using Queues 
       #       Root-b      #
       #      /      \     #
       #     L-a     R-c   #
       #    / \      / \   #
       # L-d  R-e  L-f R-g # 

# Rule of BFS is if you visit a node visit its children too or are going to visit one level(parent level), visit the next level (children level) too 
# BFS Traversal for this tree is bacdefgs

# We use queues here: 
# QUEUE:
# -------------------------------
# |\b|\a|c |d |e |  |  |  |  |  |   and so on... 
# -------------------------------
# VISITED NODES for this will be : b, a, c, d, e, f, g 
# As soon as we add a parent , we need to add its children in the queue and then pop out parent and same thing forward
# As soon as we add b's childen in the queue we remove or pop b, then add a's children and pop a out and so on ..

# Adjacency List is just a list indicating what the children of those nodes are
# Example of an adjacency list for the above graph, it is important because it applies to non-binary tree and graphs as well
# Dictionary or Adjacency list for the above graph: 
# b : [a,c]
# a : [d,e]
# d : []
# e : []
# c : [f,g]
# f : []
# g : []
# In python we represent an adjancency list using a dictionary, we have a dictionary with a key:
# The value of the node is key and the list or values of that key are the children.
# Like in the above b is the key and a,c are the values of the key

import collections


class Node :
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
 
def makeList(r) :
        if r is None :
           return
        else :
            # We are making an entry in the dictionary d defined before, here we give each node a dictionary to enter their children
            d[r.data] = []
            # Then check left and right of tree
            # If the child is left
            if r.left :
                # Example: Append 'a' which is the left child of 'b' as an item in the dictionary list of 'b'
                d[r.data].append(r.left.data)
            makeList(r.left)
            # If the child is right
            if r.right : 
                # Example: Append 'c' which is the right child of 'b' as an item in the dictionary list of 'b'
                d[r.data].append(r.right.data)
            makeList(r.right)
        return d

def bfs(al) :
    queue = collections. deque('b')
    # visited list
    visited = []

    while queue :
        node = queue.popleft()
        visited.append(node) 
        # This is list comprehension
        [queue.append(x) for x in al[node]] # or can write for x in al[node]: queue.append(x)
    print(visited)
        

if __name__ == '__main__':

    root = Node('b')
    root.left = Node('a')
    root.right = Node('c')
    root.left.left = Node('d')
    root.left.right = Node('e')
    root.right.left = Node('f')
    root.right.right = Node('g')
    
    # d is a dictionary 
    d = {}
    aList = makeList(root)
    # print(aList)
    # for ele in aList: 
    #           #key  #value or children elements
    #  print(f'{ele}:{d[ele]}')

    bfs(aList)
