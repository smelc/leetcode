# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return str(self.val) + ", " + str(self.next)

def list_node_is_zero(l : Optional[ListNode]):
    return l is None or (l.val == 0 and l.next is None)

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0, None)
        self.recurse(l1, l2, result, 0)
        if list_node_is_zero(result.next):
            result.next = None # cleanup
        return result

    def recurse(self, l1: Optional[ListNode], l2: Optional[ListNode], result: ListNode, prev_remainder: int) -> None:
        l1_zero, l2_zero = (list_node_is_zero(l1), list_node_is_zero(l2))
        l1_val = 0 if l1_zero else l1.val
        l2_val = 0 if l2_zero  else l2.val
        s = l1_val + l2_val + prev_remainder
        if s >= 10:
            remainder = 1
            s = s - 10
        else:
            remainder = 0
        result.val = s

        if l1_zero and l2_zero:
            if remainder > 0:
                result.next = ListNode(1, None)
            return

        next_result = ListNode(0, None)
        result.next = next_result

        self.recurse(None if l1_zero else l1.next,
                     None if l2_zero else l2.next,
                     next_result, remainder)

        if list_node_is_zero(next_result.next):
            next_result.next = None # cleanup

if __name__ == "__main__":
    test_lhs = ListNode(2, ListNode(4, ListNode(3)))
    test_rhs = ListNode(5, ListNode(6, ListNode(4)))

    print(Solution().addTwoNumbers(test_lhs, test_rhs))

    test_lhs = ListNode(0)
    test_rhs = ListNode(0)

    print(Solution().addTwoNumbers(test_lhs, test_rhs))

    test_lhs = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
    test_rhs = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))

    print(Solution().addTwoNumbers(test_lhs, test_rhs))
        