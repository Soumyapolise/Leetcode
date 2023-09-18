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
        if root is None:
            return ""
        
        res = ""
        
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node:
                res += str(node.val) + "#"
                q.append(node.left)
                q.append(node.right)
            else:
                res += "null#"
          
        return res
            

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None
        
        data = data.split("#")
        data = data[:-1]
        
        root = node = TreeNode(data.pop(0))
        q = deque()
        q.append(node)
        i = 0
        while q:
            key = q.popleft()
            if i < len(data):
                key.left = TreeNode(data[i])
                i += 1
                q.append(key.left)
            
            if i < len(data):
                key.right = TreeNode(data[i])
                i += 1
                q.append(key.right)
        
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))