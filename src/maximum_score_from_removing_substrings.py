# https://leetcode.com/problems/maximum-score-from-removing-substrings/?envType=daily-question&envId=2024-07-16
from typing import Any, Generic, List, Optional, TypeVar
import unittest

class Tactic:
    def __init__(self, idx:int, win:int):
        self.idx = idx
        self.win = win

    def doIt(self, s: str):
        return s[0:self.idx] + s[self.idx+2: len(s)]

def findAll(s: str, searched: str) -> List[int]:
    """" All indexes where 'searched' occurs within 's' """
    i = 0
    result: List[int] = []
    len_s = len(s)
    while (i < len_s) and (i + len(searched) <= len_s):
        if s[i:i+len(searched)] == searched:
            result.append(i)
            i+=len(searched)
        else:
            i+=1
    return result

assert findAll("abab", "ab") == [0, 2]
assert findAll("ababa", "ab") == [0, 2]
assert findAll("abab", "x") == []
assert findAll("ababfoo", "ab") == [0, 2]
assert findAll("abfooaba", "ab") == [0, 5]

T = TypeVar('T')

class Tree(Generic[T]):

    val: Optional[T]
    children: list[Any]

    def __init__(self, val: Optional[T], children: list[Any]):
        self.val = val
        self.children = children

    def __str__(self) -> str:
        return self.to_string("")

    def to_string(self, indent: str) -> str:
        result: str = indent + ("None" if not self.val else str(self.val))
        for c in self.children:
            result += "\n"
            result += c.to_string(indent + "  ")
        return result

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        top: Tree[Tactic] = Tree(None, [])
        Solution.buildTacticTree(top, s, x, y)
        return Solution.depthFirstGain(top)

    @staticmethod
    def buildTactics(s: str, x: int, y: int) -> List[Tactic]:
        return [Tactic(i, x) for i in findAll(s, "ab")] + [Tactic(i, y) for i in findAll(s, "ba")]

    @staticmethod
    def buildTacticTree(parent: Tree[Tactic], s: str, x: int, y: int):
        ts: List[Tactic] = Solution.buildTactics(s, x, y)
        for t in ts:
            next_s: str = t.doIt(s)
            new_child: Tree[Tactic] = Tree(t, [])
            parent.children.append(new_child)
            Solution.buildTacticTree(new_child, next_s, x, y)

    @staticmethod
    def depthFirstGain(t: Tree[Tactic]) -> int:
        base_gain: int = 0 if not t.val else t.val.win
        max_sub: int = 0 if not t.children else max([Solution.depthFirstGain(subt) for subt in t.children])
        return base_gain + max_sub

print (Tree(0, [Tree(1, []), Tree(2, [Tree(3, []), Tree(4, [])])]))

t: Tree[Tactic] = Tree(None, [])
print(t)
Solution.buildTacticTree(t, "ababbafoo", 1, 2)
print(t)

class TestStringMethods(unittest.TestCase):
    def test_all(self):
        self.assertEqual(Solution().maximumGain("cdbcbbaaabab", 4, 5), 19)
        self.assertEqual(Solution().maximumGain("aabbaaxybbaabb", 5, 4), 20)

if __name__ == "__main__":
    unittest.main()