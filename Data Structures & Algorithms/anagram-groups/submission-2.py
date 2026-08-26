
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Go through each word
        # Get sorted version of that word
        # Store sorted version of that word in dict
        # Add that word as value in a list to the sorted version key
        # Assume n words
        # Assume length of word is l
        # O(n * l log l) = n * l log l runtime
 
        # Go through each word
        # Go through each letter of each word
        # count the frequency of each letter and update array[ord(letter)] with freq
        # Store this arr as a tuple as a key in the hashmap
        # Go through each word and do this and have the words as values themselves
        # The runtime for this is O(n * l)
        my_dict = defaultdict(list)
        for str in strs:
            freq_arr = [0 for i in range(26)]
            for letter in str:
                letter_index = ord(letter) - ord('a')
                freq_arr[letter_index] += 1
            freq_tuple = tuple(freq_arr)
            my_dict[freq_tuple].append(str)

        return list(my_dict.values())

            

