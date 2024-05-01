class Tree:
    def __init__(self,val):
        self.val=val
        self.right=None
        self.left=None
        
que,vis=[],[]
def bfs(root):
    if root:
        que.append(root)
    while que:
        curr=que.pop(0)
        vis.append(curr.val)
        if curr.right:
            que.append(curr.right)
        if curr.left:
            que.append(curr.left)        
            
root = Tree(4)
root.left = Tree(2)
root.right = Tree(4)
root.right.left = Tree(1)
root.right.right = Tree(11)
root.left.right = Tree(9)
root.left.left = Tree(10)

bfs(root)
print(vis)