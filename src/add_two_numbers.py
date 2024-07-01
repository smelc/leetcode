# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return str(self.val) + ", " + str(self.next)

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0, None)
        self.recurse(l1, l2, result, 0)
        return result

    def recurse(self, l1: Optional[ListNode], l2: Optional[ListNode], result: ListNode, prev_remainder: int) -> None:
        if l1 is None:
            result.next = l2
            return
        if l2 is None:
            result.next = l1
            return
        s = l1.val + l2.val + prev_remainder
        if s >= 10:
            remainder = 1
            s = s - 10
        else:
            remainder = 0
        next_result = ListNode(0, None)
        result.val = s
        result.next = next_result
        self.recurse(l1.next, l2.next, next_result, remainder)

if __name__ == "__main__":
    test_lhs = ListNode(2, ListNode(4, ListNode(3)))
    test_rhs = ListNode(5, ListNode(6, ListNode(4)))

    print(Solution().addTwoNumbers(test_lhs, test_rhs))
        