class ListNode(object):
	def __init__(self, val = 0, next = None):
		self.val = val
		self.next = next

def solution1(head):
        temp = head

        while head and head.next:
            if head.next.val == head.val:
                head.next = head.next.next
            else:
                head = head.next

        return temp 

if __name__ == "__main__":
	first = ListNode(val=1)
	second = ListNode(val=1)
	third = ListNode(val=2)
	first.next = second
	second.next = third

	solution1(first)

	rv = []	
	temp = first
	while first:
		rv.append(first.val)
		first = first.next
	
	print(rv) 
