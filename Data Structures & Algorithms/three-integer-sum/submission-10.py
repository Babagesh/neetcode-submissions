class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Go through the array and subtract each number from zero
        # Store this number and its index in a hashmap
        # This is the amount two distinct numbers need to sum too 
        # Sort the array
        # [-4, -1, -1, 0, 1, 2]
       
        indices = []
        my_dict= {}
        nums.sort()
        for i, num in enumerate(nums):
            my_dict[num] = i
        left = 0
        while left < len(nums):
            start = nums[left]
            right = left + 1
            while right < len(nums):
                other = nums[right]
                my_sum = start + other
                difference = 0 - my_sum
                if difference in my_dict and my_dict[difference] > right:
                    indices.append([start, other, difference])
                while right < len(nums) and nums[right] == other:
                    right += 1
            while left < len(nums) and nums[left] == start:
                left += 1
        return indices
            