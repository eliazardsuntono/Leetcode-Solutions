class TreeNode(object):
	def __init__ (self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def isTheSame(a, b):
	if a is None and b is None:
		return True
	
	if a and b:
		return (a.val == b.val) and isTheSame(a.right, b.left) and isTheSame(a.left, b.right)

def solution1(root):
	return isTheSame(root.left, root.right)

if __name__ == "__main__":
	First = TreeNode(val=1)
	Second = TreeNode (val=2)
	Third = TreeNode(val=2)
	First.left = Second
	First.right = Third

	Fourth = TreeNode(val=3)
	Fifth = TreeNode(val=4)
	Sixth = TreeNode(val=3)
	Seventh = TreeNode(val=4)
	Second.left = Fourth
	Second.right = Fifth
	Third.left = Seventh 
	Third.right = Sixth

	print(solution1(First))
