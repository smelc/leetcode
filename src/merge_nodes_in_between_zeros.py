from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val) + ((" -> " + str(self.next)) if self.next else "")

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        Solution.go(head, head.next, 0)
        return head.next

    # Returns a fresh list
    @staticmethod
    def go(start: ListNode, cur: ListNode, acc: int) -> ListNode:
        if cur.val == 0:
            next_current = ListNode(acc)
            start.next = next_current
            if not cur.next:
                # terminal case
                return
            Solution.go(next_current, cur.next, 0)
            return
        assert cur.next
        Solution.go(start, cur.next, acc + cur.val)

if __name__ == "__main__":
    l = ListNode(0, ListNode(3, ListNode(1, ListNode(0))))
    print(l)
    print(Solution().mergeNodes(l))
    l = ListNode(0, ListNode(3, ListNode(1, ListNode(0, ListNode(4, ListNode(5, ListNode(2, ListNode(0))))))))
    print(l)
    print(Solution().mergeNodes(l))
    l = ListNode(0, ListNode(333, ListNode(711, ListNode(0, ListNode(941, ListNode(0, ListNode(614, ListNode(0, ListNode(387, ListNode(0, ListNode(245, ListNode(573, ListNode(0, ListNode(162, ListNode(710, ListNode(101, ListNode(0, ListNode(709, ListNode(795, ListNode(774, ListNode(0, ListNode(198, ListNode(773, ListNode(0, ListNode(731, ListNode(0, ListNode(962, ListNode(0, ListNode(881, ListNode(891, ListNode(886, ListNode(955, ListNode(294, ListNode(0, ListNode(601, ListNode(374, ListNode(0, ListNode(625, ListNode(0, ListNode(271, ListNode(0, ListNode(665, ListNode(0, ListNode(651, ListNode(413, ListNode(0, ListNode(767, ListNode(0, ListNode(617, ListNode(0, ListNode(837, ListNode(0, ListNode(521, ListNode(0, ListNode(476, ListNode(114, ListNode(0, ListNode(364, ListNode(154, ListNode(0, ListNode(744, ListNode(0, ListNode(13, ListNode(967, ListNode(0, ListNode(908, ListNode(149, ListNode(219, ListNode(0, ListNode(109, ListNode(483, ListNode(731, ListNode(688, ListNode(962, ListNode(0, ListNode(289, ListNode(894, ListNode(0, ListNode(292, ListNode(846, ListNode(130, ListNode(0, ListNode(107, ListNode(0, ListNode(175, ListNode(0))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
    print(Solution().mergeNodes(l))