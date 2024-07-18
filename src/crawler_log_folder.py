from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        result = 0
        for i in range(len(logs)):
            match logs[i]:
                case "../":
                    result = max(0, result - 1)
                case "./":
                    pass
                case _:
                    result += 1
        return result
