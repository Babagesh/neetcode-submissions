from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counter = Counter(t)
        num_letters = len(t)
        min_window = float('inf')
        left = 0
        right = 0
        best_left, best_right = 0, 0
        while right < len(s):
            char = s[right]
            if char in t_counter:
                if t_counter[char] > 0:
                    num_letters -= 1
                t_counter[char] -= 1
            right += 1
            while num_letters == 0:
                cur_length = right - left + 1
                if cur_length < min_window:
                    best_left = left
                    best_right = right
                    min_window = cur_length
                left_char = s[left]
                if left_char in t_counter:
                    t_counter[left_char] += 1
                    if t_counter[left_char] > 0:
                        num_letters += 1
                left += 1
        if min_window == float('inf'):
            return ""
            
        return s[best_left : best_right]
       




        