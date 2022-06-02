class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
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
 

# Declaring the vector function to store 
# in, post, pre order values
pre,post,In = [],[],[]
 
# Calling the function
PostPreInOrderInOneFlowRecursive(root, pre, post, In)
 
# Print the values of Pre order, Post order
# and In order
print("Pre Order : ",end = "")
for i in pre:
    print(i,end = " ")
 
print()
print("Post Order : ",end = "")
for i in post:
    print(i,end = " ")
print()
print("In Order : ",end = "")
for i in In:
    print(i,end = " ")
    
