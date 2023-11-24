class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


tree = []
# Tạo một cây nhị phân ví dụ
#      1
#     / \
#    2   3
#   / \ / \
#  4  5 6  7

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)


def swap_left_right(roots):
    # Nếu root là None hoặc là nút lá, không làm gì
    if roots is None or (roots.left is None and roots.right is None):
        return
    # Đổi chỗ left và right của root
    roots.left, roots.right = roots.right, roots.left
    # Đệ quy cho các nút con theo thứ tự mới
    swap_left_right(roots.left)
    swap_left_right(roots.right)


def print_tree(node):
    # If node is None, do nothing
    if node is None:
        return
    # Print the data of the node
    tree.append(node.data)
    # Recursively print the left subtree
    print_tree(node.left)
    # Recursively print the right subtree
    print_tree(node.right)


print_tree(root)
print(tree)

swap_left_right(root)
print_tree(root)

print(tree[len(tree) // 2:])
