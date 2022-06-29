class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.lnode = None
        self.rnode = None
        self.parent = None

class BST():
    def __init__(self):
        self.root = None

    # def insert(self, node, val):
    #     if not node:
    #         node = BiTreeNode(val)
    #     elif val <node.data:


a = BiTreeNode("A")
b = BiTreeNode("B")
c = BiTreeNode("C")
d = BiTreeNode("D")
e = BiTreeNode("E")
f = BiTreeNode("F")
g = BiTreeNode("G")

e.lnode = a
e.rnode = g
a.rnode = c
c.lnode = b
c.rnode = d
g.rnode = f

root = e


def pre_order(root):
    if root:
        print(root.data, end=',')
        pre_order(root.lnode)
        pre_order(root.rnode)


def in_order(root):
    if root:
        in_order(root.lnode)
        print(root.data, end=',')
        in_order(root.rnode)


def post_order(root):
    if root:
        post_order(root.lnode)
        post_order(root.rnode)
        print(root.data, end=',')


pre_order(root)
print("\n")
in_order(root)
print("\n")
post_order(root)
