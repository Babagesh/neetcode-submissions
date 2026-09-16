class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Have a set and just iterate till a charcter in the hashmap not encountered
        # Once a duplicate encountered, we know the substring streak is over
        # However the streak can still continue for the character after the duplicate
        # So we need to keep a track of a pointer running, and a pointer which keeps track of the character after the found duplicate
        # We iterate left to the index after the duplicate and then keep moving right till a duplciate found
        # Do this until right reaches end or another duplicate is found
        # Make sure whenever duplicate found or end is reached, we calculate the length
        # O(n) runtime and O(n) space
        # 
        left = 0
        right = 0
        max_length = 0
        my_dict = {}
        end_duplicate = False
        while right < len(s):
            current_char = s[right]
            if current_char in my_dict:
                length = right - left
                if length > max_length:
                    max_length = length
                duplicate_index = my_dict[current_char]
                if duplicate_index >= left:
                    left = duplicate_index + 1
                del my_dict[current_char]
                my_dict[current_char] = right
            else:
                my_dict[current_char] = right
            right += 1
                
        final_length = right - left
        max_length = final_length if final_length > max_length else max_length
        return max_length 

