class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
       # Find most frequent character and subtract from total length
       # that's how many need to be replaced
       # Sliding window
        # AAABBBBBA
        left = 0
        right = 0
        letter_freq = {} # store each character and its frequency
        max_freq = 0
        while right < len(s):
            addition = s[right]
            addition_freq = letter_freq.get(addition, 0) + 1
            letter_freq[addition] = addition_freq
            if addition_freq > max_freq:
                max_freq = addition_freq
            replace_count = (right - left + 1) - max_freq
            if replace_count > k:
                letter_freq[s[left]] -= 1
                left += 1
                right += 1
            else:
                right += 1
        return right - left

    


       
