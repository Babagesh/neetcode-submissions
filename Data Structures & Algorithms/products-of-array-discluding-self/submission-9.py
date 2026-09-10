class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Sliding window where we need to have a frame of reference and capture
        # everything before and after(value of multiplication) and when we traverse
        # we multiply by the new element added to the 
        zero_count = nums.count(0)
        if zero_count > 1:
            return [0 for i in range(len(nums))]
        zero_product = 1
        actual_product = 1
        for i in range(0, len(nums)):
            if nums[i] != 0:
                zero_product *= nums[i]
            actual_product *= nums[i]
        output = []
        for num in nums:
            if num == 0:
                output.append(zero_product)
            else:
                output.append(actual_product // num)
        return output
