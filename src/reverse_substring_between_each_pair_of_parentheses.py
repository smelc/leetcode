from typing import Any, Optional

class Chunk:

    prefix: Optional[str]
    nested: Optional[Any] # str or Chunk
    suffix: Optional[str]

    def __init__(self, prefix, nested, suffix):
        self.prefix = prefix
        self.nested = nested
        self.suffix = suffix

    def reduce(self) -> str:
        p = self.prefix if self.prefix else ""
        n = self.nested.reduce() if self.nested else ""
        s = self.suffix if self.suffix else ""
        return Chunk.reverse(p + n + s)

    def __str__(self):
        p = Chunk.coerce(self.prefix)
        n = "None" if self.nested is None else str(self.nested)
        s = Chunk.coerce(self.suffix)
        return "Chunk(" + p + ", " + n + ", " + s + ")"

    @staticmethod
    def coerce(s: str):
        return "None" if s is None else s

    @staticmethod
    def reverse(s: str):
        result = ""
        for i in range(len(s)):
            result = s[i] + result
        return result

class Solution:
    def reverseParentheses(self, s: str) -> str:
        s = s.replace("()", "") # hacky

        start = 0
        end = len(s) - 1

        if start == end:
            return ""

        top_level = Chunk(None, None, None)
        current_chunk = top_level

        while start < end and start < len(s) and 0 <= end:
            parse_start = True
            parse_end = True
            start_str = ""
            end_str = ""

            lonely = None

            while (parse_start or parse_end) and start < end:
                if parse_start:
                    start_char=s[start]
                    start+=1
                    if start_char == "(":
                        parse_start = False
                    else:
                        start_str+=start_char
                if parse_end:
                    end_char=s[end]
                    end-=1
                    if end_char == ")":
                        parse_end = False
                    else:
                        end_str = end_char + end_str
                if start == end:
                    c = s[start]
                    if c in ["(", ")"]:
                        break
                    lonely = Chunk(c, None, None)
                    break

            next_chunk = Chunk(start_str, lonely, end_str)
            current_chunk.nested = next_chunk
            current_chunk = next_chunk

        print(top_level)
        result = top_level.reduce()
        print(result)

        return result

if __name__ == "__main__":
    assert Solution().reverseParentheses("(u(love)i)") == "iloveu"
    assert Solution().reverseParentheses("(ed(et(oc))el)") == "leetcode"
    assert Solution().reverseParentheses("a(bcdefghijkl(mno)p)q") == "apmnolkjihgfedcbq"
    assert Solution().reverseParentheses("(abcd)") == "dcba"
    assert Solution().reverseParentheses("vdgzyj()") == "vdgzyj"