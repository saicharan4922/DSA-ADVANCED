# Implement Binary tree 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            self._insert(val, self.root)

    def _insert(self, val, node):
        if val < node.val:
            if not node.left:
                node.left = TreeNode(val)
            else:
                self._insert(val, node.left)
        else:
            if not node.right:
                node.right = TreeNode(val)
            else:
                self._insert(val, node.right)

    def search(self, val):
        return self._search(val, self.root)

    def _search(self, val, node):
        if not node:
            return False
        elif node.val == val:
            return True
        elif val < node.val:
            return self._search(val, node.left)
        else:
            return self._search(val, node.right)
tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(1)
tree.insert(4)

print(tree.search(4))  
print(tree.search(6))  


# Find height of a given tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            self._insert(val, self.root)

    def _insert(self, val, node):
        if val < node.val:
            if not node.left:
                node.left = TreeNode(val)
            else:
                self._insert(val, node.left)
        else:
            if not node.right:
                node.right = TreeNode(val)
            else:
                self._insert(val, node.right)

    def height(self):
        if not self.root:
            return 0
        else:
            return self._height(self.root)

    def _height(self, node):
        if not node:
            return 0
        else:
            left_height = self._height(node.left)
            right_height = self._height(node.right)
            return max(left_height, right_height) + 1
tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(1)
tree.insert(4)

print(tree.height())  



# Perform Pre-order, Post-order, In-order traversa


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            self._insert(val, self.root)

    def _insert(self, val, node):
        if val < node.val:
            if not node.left:
                node.left = TreeNode(val)
            else:
                self._insert(val, node.left)
        else:
            if not node.right:
                node.right = TreeNode(val)
            else:
                self._insert(val, node.right)

    def pre_order(self):
        self._pre_order(self.root)

    def _pre_order(self, node):
        if node:
            print(node.val, end=' ')
            self._pre_order(node.left)
            self._pre_order(node.right)

    def in_order(self):
        self._in_order(self.root)

    def _in_order(self, node):
        if node:
            self._in_order(node.left)
            print(node.val, end=' ')
            self._in_order(node.right)

    def post_order(self):
        self._post_order(self.root)

    def _post_order(self, node):
        if node:
            self._post_order(node.left)
            self._post_order(node.right)
            print(node.val, end=' ')
tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(1)
tree.insert(4)

print("Pre-order traversal:", end=' ')
tree.pre_order()  

print("\nIn-order traversal:", end=' ')
tree.in_order()  

print("\nPost-order traversal:", end=' ')
tree.post_order()  



# Function to print all the leaves in a given binary tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            self._insert(val, self.root)

    def _insert(self, val, node):
        if val < node.val:
            if not node.left:
                node.left = TreeNode(val)
            else:
                self._insert(val, node.left)
        else:
            if not node.right:
                node.right = TreeNode(val)
            else:
                self._insert(val, node.right)

    def print_leaves(self):
        self._print_leaves(self.root)

    def _print_leaves(self, node):
        if not node:
            return
        if not node.left and not node.right:
            print(node.val, end=' ')
        else:
            self._print_leaves(node.left)
            self._print_leaves(node.right)
tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(1)
tree.insert(4)
tree.insert(6)
tree.insert(9)

tree.print_leaves()  


# Implement BFS (Breath First Search) and DFS (Depth First Search)


from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                print(node, end=' ')
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)

    def dfs(self, start):
        visited = set()
        self._dfs(start, visited)

    def _dfs(self, node, visited):
        visited.add(node)
        print(node, end=' ')
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self._dfs(neighbor, visited)
graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(3, 3)

print("BFS Traversal:")
graph.bfs(2)


print("\nDFS Traversal:")
graph.dfs(2)



# Find sum of all left leaves in a given Binary Tree

def sum_of_left_leaves(root):
    if root is None:
        return 0

    if root.left is not None and root.left.left is None and root.left.right is None:
        return root.left.val + sum_of_left_leaves(root.right)

    return sum_of_left_leaves(root.left) + sum_of_left_leaves(root.right)
# Example binary tree
#       3
#     /   \
#    9     20
#  /  \   /  \
# 6   12 15   7

root = TreeNode(3)
root.left = TreeNode(9)
root.left.left = TreeNode(6)
root.left.right = TreeNode(12)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(sum_of_left_leaves(root)) 


# Find sum of all nodes of the given perfect binary tree

def sum_perfect_binary_tree(root):
    if root is None:
        return 0


    height = 0
    node = root
    while node is not None:
        height += 1
        node = node.left

    num_nodes = (2 ** height) - 1

    return num_nodes * root.val + sum_perfect_binary_tree(root.left) + sum_perfect_binary_tree(root.right)
# Example perfect binary tree
#       5
#     /   \
#    3     7
#  /  \   /  \
# 1    2 6    8

root = TreeNode(5)
root.left = TreeNode(3)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)
root.right = TreeNode(7)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)

print(sum_perfect_binary_tree(root)) # Output: 32


# Count subtress that sum up to a given value x in a binary tree


def count_subtrees_with_sum_x(root, x):
    count = 0

    def helper(node):
        nonlocal count
        if node is None:
            return 0

        left_sum = helper(node.left)
        right_sum = helper(node.right)

        # Calculate the sum of the subtree rooted at this node
        subtree_sum = left_sum + right_sum + node.val

        # If the sum of the subtree is equal to x, increment the count
        if subtree_sum == x:
            count += 1

        return subtree_sum

    helper(root)
    return count


# Example binary tree
#       5
#     /   \
#    3     2
#  /  \   /  \
# 4    6 1    7

root = TreeNode(5)
root.left = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(6)
root.right = TreeNode(2)
root.right.left = TreeNode(1)
root.right.right = TreeNode(7)

print(count_subtrees_with_sum_x(root, 9)) 


# Find maximum level sum in Binary Tree

from collections import deque

def max_level_sum(root):
    if root is None:
        return 0

    queue = deque([root])
    max_sum = root.val

    while queue:
        level_size = len(queue)
        level_sum = 0

        for i in range(level_size):
            node = queue.popleft()
            level_sum += node.val

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        max_sum = max(max_sum, level_sum)

    return max_sum
# Example binary tree
#       1
#     /   \
#    2     3
#  /  \     \
# 4    5     6

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

print(max_level_sum(root)) 


# Print the nodes at odd levels of a tree

def print_odd_levels(root):
    def traverse(node, level):
        if node is None:
            return

        if level % 2 == 1:
            print(node.val)

        traverse(node.left, level+1)
        traverse(node.right, level+1)

    traverse(root, 1)
# Example binary tree
#       1
#     /   \
#    2     3
#  /  \   / \
# 4    5 6   7

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print_odd_levels(root) 


