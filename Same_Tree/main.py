class TreeNode(object):
	def __init__(self, val = 0, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right

def solution1(p,q):
	if p is None and q is None:
		return True
	
	if p and q:
		return (p.val == q.val) and solution1(p.left, q.left) and solution1(p.right, q.right)

if __name__ == "__main__":
	#First Tree Node
	first = TreeNode(val=1)
	second = TreeNode(val=2)
	third = TreeNode(val=3)
	first.left = second
	first.right = third

	# Second Tree Node
	First = TreeNode(val=1)
	Second = TreeNode(val=2)
	Third = TreeNode(val=3)
	First.left = Second
	First.right = Third

	print(solution1(first, First))

