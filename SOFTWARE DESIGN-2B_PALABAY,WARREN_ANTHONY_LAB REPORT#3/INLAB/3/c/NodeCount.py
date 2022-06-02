class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
        
def getfullCount(root):
    
    if (root == None):
        return 0
    
    res = 0
    if (root.left and root.right):
        res += 1
    
    res += (getfullCount(root.left) +
            getfullCount(root.right))
    return res

def getLeafCount(node):
    if node is None:
        return 0
    if(node.left is None and node.right is None):
        return 1
    else:
        return getLeafCount(node.left) + getLeafCount(node.right)
# Function for traversing tree using
# preorder postorder and inorder method
def PostPreInOrderInOneFlowRecursive(root, pre, post, In):
 
    # Return if root is None
    if (root == None):
        return
 
    # Pushes the root data into the pre
    # order vector
    pre.append(root.data)
 
    # Recursively calls for the left node
    PostPreInOrderInOneFlowRecursive(root.left, pre, post, In)
 
    # Pushes node data into the inorder vector
    In.append(root.data)
 
    # Recursively calls for the right node
    PostPreInOrderInOneFlowRecursive(root.right, pre, post, In)
 
    # Pushes the node data into the Post Order
    # Vector
    post.append(root.data)
 
# Driver Code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.left.left.left.right= Node(12)
root.left.right.left = Node(9)
root.right.right.left = Node(10)
root.right.right.right = Node(11)
 
print ("Leaf node count of the tree is %d" %(getLeafCount(root)))
print("full node count of the tree is %d" %getfullCount(root))
