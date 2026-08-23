from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frequencies = [0 for i in range(26)]
        if len(s) != len(t):
            return False
        for c in s:
            frequencies[ord(c) - ord('a')] += 1
        for ch in t:
            frequencies[ord(ch) - ord('a')] -= 1
        for num in frequencies:
            if num != 0:
                return False
        return True