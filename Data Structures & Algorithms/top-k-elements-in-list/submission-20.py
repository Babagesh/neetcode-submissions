from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = [[] for i in range(len(nums) + 1)]
        count_dict = Counter(nums)
        for element, count in list(count_dict.items()):
            counts[count].append(element)
        k_elements = []
        k_found = 0
        for i in range(len(nums), -1, -1):
            if counts[i]:
                for ele in counts[i]:
                    k_elements.append(ele)
                    k_found += 1       
                    if k_found == k:
                        return k_elements
                        
        return k_elements

