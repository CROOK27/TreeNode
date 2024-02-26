class TreeNode:
    class Item:
        value = None
        right = None 
        left = None
        def __init__(self, value):
            self.value = value

    head:Item = None
    
    def __len__(self):
        current=self.head
        def Tree_traversal(Tree):
            res = []
            if Tree:
                res = Tree_traversal(Tree.left)
                res.append(Tree.value)
                res = res + Tree_traversal(Tree.right)
            return res
        return len(Tree_traversal(current))
    
    def append_by_Value(self, value):
        item = TreeNode.Item(value)
        if self. head is None:
           self. head = item
           return
        current=self.head
        while True:
            if value <= current.value and current.left is None:
                current.left=item
                return
            elif value >= current.value and current.right is None:
                current.right=item
                return
            if current.value >= value:
                current=current.left
            elif current.value <= value: 
                current=current.right
               
    def remove_by_Vallue(self,value):
        if self.head is None:
            raise NameError("Элементов нет")
        if self. head.value == value:
            if self.head.left is not None or self.head.right is not None:
                raise ValueError("Error")
            self. head = None
            return
        current=self.head
        while True:
            if value == current.left.value:
                if current.left.left is not None or current.left.right is not None:
                    raise ValueError("Error")
                current.left=None
                return
            elif value == current.right.value :
                if current.right.left is not None or current.right.right is not None:
                    raise ValueError("Error")
                current.right=None
                return
            if current.value >= value:
                current=current.left
            elif current.value <= value: 
                current=current.right
            if current is None:
                raise ValueError("Error")
