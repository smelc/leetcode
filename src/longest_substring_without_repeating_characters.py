class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        previous_longest = ""

        # dict from already-seen character to its position
        current_longest_set: dict[str, int] = {}
        current_longest = ""

        max = len(s)
        i = 0

        while i < max:
            c: str = s[i]
            if c in current_longest_set.keys():
                # A repeatition
                if len(current_longest) > len(previous_longest):
                    # Record it
                    previous_longest = current_longest
                # Restart from position after the first occurrence of the repeated character
                i = current_longest_set[c] + 1

                # Reset
                current_longest_set = {}
                current_longest = ""
                continue
            else:
                current_longest_set[c] = i
                current_longest += c
                # Continue
                i += 1

        if len(current_longest) > len(previous_longest):
            # Loop finished while looking at the longest substring without duplicates
            previous_longest = current_longest

        # print(previous_longest)
        return len(previous_longest)


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("abcabcbb"))
    print(Solution().lengthOfLongestSubstring("bbbb"))
    print(Solution().lengthOfLongestSubstring("pwwkew"))
    print(Solution().lengthOfLongestSubstring("dvdf"))
