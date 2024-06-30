class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solution(l1, l2):
        rv = ListNode()
        cur = rv
        r = 0
        while l1 and l2:
            num = r + l1.val + l2.val

            if num > 9:
                r = num / 10
                num = num % 10
            else:
                r = 0

            nxt = ListNode(val=num,next=None)
            cur.next= nxt
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        
        if l1:
            while l1:
                num = r + l1.val

                if num > 9:
                    r = num / 10
                    num = num % 10
                else:
                    r = 0

                nxt = ListNode(val=num,next=None)
                cur.next = nxt
                cur = cur.next
                l1 = l1.next
        else:
            while l2:
                num = r + l2.val

                if num > 9:
                    r = num / 10
                    num = num % 10
                else:
                    r = 0
            
                nxt = ListNode(val=num,next=None)
                cur.next = nxt
                cur = cur.next
                l2 = l2.next

        if r != 0:
            nxt = ListNode(val=r, next=None)
            cur.next = nxt

        return rv.next

if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    rv = solution(l1, l2)
    while rv:
        print(rv.val)
        rv = rv.next