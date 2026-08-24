class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for index, num in enumerate(nums):
            difference = target - num
            if difference in my_dict:
                difference_index = my_dict[difference]
                return [difference_index, index]
            else:
                my_dict[num] = index
        return False
