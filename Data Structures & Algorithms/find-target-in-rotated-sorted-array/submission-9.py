class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # .find function in python returns first index(O(n)) runtime
        # Since we know sorted, we can try a binary search type algorithm
        # We can use the last element as referece
        # If last elemet is greater than our current, than we know that from current to end only increasing. We check if target is within that range.
        # THen we check if last element is less than current
        # If less than current, but target is less than the last element, target is in right side
        # Otherwise target is in left side
        right = len(nums) - 1
        left = 0
        while left <= right:
            middle = (left + right) // 2
            end_element = nums[right]
            middle_element = nums[middle]
            if middle_element == target:
                return middle
            elif end_element > middle_element and target <= end_element and target > middle_element  or end_element < middle_element and target <= end_element or end_element < middle_element and target > middle_element:
                left = middle + 1
            else:
                right = middle - 1
        return -1
            
