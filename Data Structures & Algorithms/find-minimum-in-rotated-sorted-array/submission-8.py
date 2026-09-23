class Solution:
    def findMin(self, nums: List[int]) -> int:
        right = len(nums) - 1
        left = 0
        while left < right:
            middle = (left + right) // 2
            middle_element = nums[middle]
            last_element = nums[right]
            if middle_element < last_element:
                right = middle
            else:
                left = middle + 1
        return nums[left]

        

            