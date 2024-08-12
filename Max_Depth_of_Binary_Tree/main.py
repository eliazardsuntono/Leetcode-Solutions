from collections import deque

class TreeNode(object):
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right	
def solution1(root):
	if root is None:
		return 0
	
	left = solution1(root.left)
	right = solution1(root.right)

	if left > right:
		return left + 1
	else:
		return right + 1

def solution2(root):
	if root is None:
		return 0
	
	count = 1
	ans = 0
	que = deque([root])

	while que:
		for i in range(len(que)):
			node = que.popleft()
			if not node.left and not node.right:
				ans = max(count, ans)
			if node.left:
				que.append(node.left)
			if node.right:  # Fixed typo: changed "root.right" to "node.right"
				que.append(node.right)
			count += 1
	return ans

if __name__ == "__main__":
	First = TreeNode(val=1)
	Second = TreeNode(val=2)
	Third = TreeNode(val=3)
	
	First.left = Second
	First.right = Third

	print(solution1(First))
	print(solution2(First))	
