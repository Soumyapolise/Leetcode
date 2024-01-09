# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        
        stack = [root]
        
        while stack:
            node = stack.pop(0)
            if node is None:
                res.append("None")
                continue
            
            res.append(node.val)
            
            stack.append(node.left)
            stack.append(node.right)
        
        return " ".join(str(x) for x in res)
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(" ")
        if data == ['None']:
            return None
        res = []
        for x in data:
            if x != "None":
                res.append(int(x))
            else:
                res.append(x)
        
        root = TreeNode(res.pop(0))
        
        stack = [root]
        while stack:
            node = stack.pop(0)
            if not node:
                continue
            l = res.pop(0)
            if l == "None":
                node.left = None
            else:
                node.left = TreeNode(l)
                
            r = res.pop(0)
            if r == "None":
                node.right = None
            else:
                node.right = TreeNode(r)
            
            stack.append(node.left)
            stack.append(node.right)
        
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))