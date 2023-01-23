class Node:
  def __init__(self, data):
    self.data = data
    self.right_child = None
    self.left_child = None

class Tree:
  def __init__(self):
    self.root_node = None

  def insert(self, data):
    node = Node(data)
    if self.root_node is None:
      self.root_node = node
      return self.root_node
    else:
      current = self.root_node
      parent = None
      while True:
        parent = current
        if node.data < parent.data:
          current = current.left_child
          if current is None:
            parent.left_child = node
            return self.root_node
          else:
            current = current.right_child