# Trees in Data Structures (DSA)
# A Tree is a non-linear data structure that represents a hierarchy. It consists of nodes connected by edges. 
# The topmost node is called the root, and each node can have child nodes.

# Basic Tree Terminology
# Root – The first node of the tree.
# Parent – A node that has child nodes.
# Child – A node that has a parent node.
# Siblings – Nodes that share the same parent.
# Leaf – A node that has no children.
# Depth – Number of edges from the root to a node.
# Height – Number of edges from a node to the deepest leaf.
# Subtree – A tree formed from a node and its descendants.
# Binary Tree – A tree where each node has at most 2 children.
# Types of Trees
# 1️⃣ Binary Tree
# A tree where each node has at most two children.

#        1
#       / \
#      2   3
#     / \
#    4   5

# 2️⃣ Binary Search Tree (BST)
# A binary tree where:

# The left child is smaller than the parent.
# The right child is greater than the parent.

#        10
#       /  \
#      5   15
#     / \    \
#    2   7   20
# ✅ Operations: Insertion, Deletion, Search (O(log N) on average)

# 3️⃣ Balanced Binary Tree
# A binary tree where the height difference between the left and right subtrees is at most 1.

# AVL Tree (Self-balancing using rotations)
# Red-Black Tree (Used in maps & sets)

# 4️⃣ N-ary Tree
# A tree where each node can have more than two children.

# 5️⃣ Heap (Binary Heap)
# A complete binary tree that follows:

# Min-Heap: Parent is smaller than children.
# Max-Heap: Parent is greater than children.
# 6️⃣ Trie (Prefix Tree)
# Used for searching words efficiently in dictionaries.

# Tree Traversals
# 1️⃣ Depth-First Search (DFS)
# ✅ Uses recursion or stack.

# Three types:

# Inorder (LNR): Left → Root → Right
# Preorder (NLR): Root → Left → Right
# Postorder (LRN): Left → Right → Root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)
        
# 2️⃣ Breadth-First Search (BFS) / Level Order Traversal
# ✅ Uses a queue.
# ✅ Visits nodes level by level.

from collections import deque

def level_order(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.data, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
            
# Common Tree Questions
# 1️⃣ Find the height of a tree
# 2️⃣ Check if a tree is a BST
# 3️⃣ Lowest Common Ancestor (LCA) of two nodes
# 4️⃣ Convert a BST to a Balanced BST
# 5️⃣ Print all root-to-leaf paths
# 6️⃣ Mirror a Binary Tree
# 7️⃣ Check if two trees are identical
# 8️⃣ Find the diameter of a tree

class Node():
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinarySearchTree():
    
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
                
    def contains(self, value):
        temp = self.root
        while temp:
            if temp.value == value:
                return True
            if value < temp.value:
                temp = temp.left
            else:
                temp = temp.right
        return False
        
my_tree = BinarySearchTree()
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)


print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)
print(my_tree.contains(5))