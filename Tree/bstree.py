class TreeNode:

  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value
  
  def insert(self, value):
    if self.value > value:
      if self.left is None:
        self.left = TreeNode(value)
      else:
        self.left.insert(value)
    # elif self.value < value:
    else:
      if self.right is None:
        self.right = TreeNode(value)
      else:
        self.right.insert(value)
 
  def inorder_traversal(self):
    if self.left:
      self.left.inorder_traversal()
    print(self.value)
    if self.right:
      self.right.inorder_traversal()

  def preorder_traversal(self):
    print(self.value)
    if self.left:
      self.left.preorder_traversal()
    if self.right:
      self.right.preorder_traversal()

  def postorder_traversal(self):
    if self.left:
      self.left.postorder_traversal()
    if self.right:
      self.right.postorder_traversal()
    print(self.value)

  def find(self, value):
    if value < self.value:
      if self.left is None:
        return print("Element does not exist")
      else:
        return self.left.find(value)
    elif value > self.value:
      if self.right is None:
        return print("Element does not exist")
      else:
        return self.right.find(value)
    else:
      return True
  
  def delete(self, value):
    if value < self.value:
      if self.left is None:
        return print("Element does not exist")
      else:
        return self.left.delete(value)
    elif value > self.value:
      if self.right is None:
        return print("Element does not exist")
      else:
        return self.right.delete(value)
    else:
      if self.left == None and self.right == None:
        self.value = None
        print("leaf node deleted")
      elif self.left == None or self.right == None:
        if self.left is None:
          self.value = self.right.value
          self.right = None
          print("node only with right child deleted")
        elif self.right is None:
          self.value = self.left.value
          self.left = None
          print("node only with left child deleted")


tree = TreeNode(6)

tree.insert(5)
tree.insert(2)
tree.insert(3)
tree.insert(4)


# tree.inorder_traversal()
tree.preorder_traversal()
tree.delete(3)
tree.preorder_traversal()
# tree.postorder_traversal()

# print(tree.find(2))
# print(tree.delete(5))