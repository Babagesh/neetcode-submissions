class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # You can sort and go through nums(n log n)
        # Do a while loop and keep increment until next element is 1 more than previous. Keep a counter 
        # If not 1 more, than update previous to next, and then increment next to one after
        # Do until next hits end

        # Convert nums into a set
        # Go through nums
        # Then increment loop from nums(while loop) until an element is not found
        # Keep track of length(latest found - initial)
        #O(n^2)


        count = 0
        my_set = set(nums)
        max_length = 0
        for num in nums:
            if num - 1 not in my_set:
                while num in my_set:
                    num += 1
                    count += 1
                if count > max_length:
                    max_length = count
                count = 0
            else:
                continue
        return max_length

