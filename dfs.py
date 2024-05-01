class Node:
    def __init__(self,value):
        self.val=value 
        self.left=None
        self.right=None
st,vis=[],[]        

def dfs(root):
    if root:
        vis.append(root.val)
        if root.right:
            st.append(root.right)
        if root.left:
            st.append(root.left)
        if st:
            dfs(st.pop())
        
            
        
    
node1=Node(0)
node1.left=Node(1)
node1.right=Node(2)
node1.left.left=Node(3)
node1.left.right=Node(4)
node1.right.left=Node(5)
node1.right.right=Node(6)

dfs(node1)
print(vis)