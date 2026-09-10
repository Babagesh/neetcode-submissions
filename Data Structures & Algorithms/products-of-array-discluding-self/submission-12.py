class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffix = []
        prefix = []
        product = 1
        for i in range(len(nums)):
            prefix.append(product)
            product *= nums[i]
        # [1, 1, 2, 8]
        product = 1
        for i in range(len(nums) - 1, -1, -1):
            suffix.append(product)
            product *= nums[i]
        suffix.reverse()
        output = []
        for pre, suff in zip(prefix, suffix):
            output.append(pre * suff)
        return output
