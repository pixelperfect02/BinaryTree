# Adjacency List, Python Code By Archie Verma
       #       Root-b      #
       #      /      \     #
       #     L-a     R-c   #
       #    / \      / \   #
       # L-d  R-e  L-f R-g # 
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
    for ele in aList: 
              #key  #value or children elements
     print(f'{ele}:{d[ele]}')
        


# Just FYI if we were to make an adjacency matrix this is how we can draw it:
# Adjacency matrix  
#   a b c d e f g
# a - 1 0 1 1 0 0
# b 1 - 1 2 2 2 2 
# c 0 1 - 0 0 1 1
# d 1 2 0 - 0 0 0 
# e 1 2 0 0 - 0 0 
# f 0 2 1 0 0 - 0
# g 0 2 1 0 0 0 -
# Some 0s might not be 0s in the matrix (could be wrong but we get how to do it based on the example)
