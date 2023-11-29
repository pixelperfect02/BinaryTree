# Depth First Search (DFS) using recursion, Python Code - Algorithm  using Stacks by Archie Verma
       #       Root-b      #
       #      /      \     #
       #     L-a     R-c   #
       #    / \      / \   #
       # L-d  R-e  L-f R-g # 
# We only check one child at a time in DFS, we check the node or parent and only place one child in the stack, in stack we add first element at the bottom
# We use Stacks for DFS
# STACK (\ represents pop or remove):
#  ___
# | g\|
#  ---
# | f\|
#  ---
# | c\|
#  ---
# | e\|
#  ---
# | d\| 
#  ---
# | a\|
#  ---
# | b\|
#  ---
# Visted Nodes :badecfg (from left)
# Visted Nodes :bcgfaed (from right)
# Now 'd' doesn't have any children so we are going to pop it or remove it from the stack, 
# Now again we will check the node below which is 'a' if it doesn't have any univisited children we pop or remove it but in this case it does which is 'e'
# So we place 'e' in the stack and also in the visited list now
# Now we check for left child first if there is any child we put in stack and visited node if no child which is the case here we pop 'e'
# Now we go up and check for unvisited children and so on - in this case 'a' is up no unvisited children so we pop it, next we go to 'b'
# 'b' has one unvisited child 'c' so we place it in stack and unvisited nodes, now check 'c', it has 'f' on the left, 
# Now check 'f', no children found pop 'f', go up to 'c' ,one child found on the right 'g' we place it 
# At the end all the stack elements will be popped

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def makeList(r):
    if r is None:
        return []
    else:
        left_children = makeList(r.left)
        right_children = makeList(r.right)
        return [r.data] + left_children + right_children

def dfs_recursive(node):
    if node is not None:
        print(node.data, end=' ')  # Process the current node
        dfs_recursive(node.left)   # Recursively visit the left subtree
        dfs_recursive(node.right)  # Recursively visit the right subtree

if __name__ == '__main__':
    root = Node('b')
    root.left = Node('a')
    root.right = Node('c')
    root.left.left = Node('d')
    root.left.right = Node('e')
    root.right.left = Node('f')
    root.right.right = Node('g')

    # DFS using recursion
    print("DFS Recursive:")
    dfs_recursive(root)

# DFS without recursion
# import collections
# class Node :
#     def __init__(self, data):
#         self.left = None
#         self.right = None
#         self.data = data
 
# def makeList(r) :
#         if r is None :
#            return
#         else :
#             # We are making an entry in the dictionary d defined before, here we give each node a dictionary to enter their children
#             d[r.data] = []
#             # Then check left and right of tree
#             # If the child is left
#             if r.left :
#                 # Example: Append 'a' which is the left child of 'b' as an item in the dictionary list of 'b'
#                 d[r.data].append(r.left.data)
#             makeList(r.left)
#             # If the child is right
#             if r.right : 
#                 # Example: Append 'c' which is the right child of 'b' as an item in the dictionary list of 'b'
#                 d[r.data].append(r.right.data)
#             makeList(r.right)
#         return d

# # can print from left or right 
# def dfs(al) :
#     stack = ['b']
#     visited = []
#     while stack :
#         node = stack.pop()
#         if node not in visited :
#             visited.append(node)
#             [stack.append(x) for x in al[node]]
#     print(visited)


# if __name__ == '__main__':

#     root = Node('b')
#     root.left = Node('a')
#     root.right = Node('c')
#     root.left.left = Node('d')
#     root.left.right = Node('e')
#     root.right.left = Node('f')
#     root.right.right = Node('g')

#     d = {}
#     aList = makeList(root)
#     dfs(aList)

