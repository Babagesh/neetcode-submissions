class Solution:

    def encode(self, strs: List[str]) -> str:
        # traverse string length
        # After traversing string length, traverse until # is found or end of string
        # Keep adding whatever you find till # after length of string is traversed
        # From there once # is found, traverse further whatever length was found till #
        # Repeat
        char_arr = []
        for string in strs:
            char_arr.append(str(len(string)))
            char_arr.append("#")
            char_arr.append(string)
        return "".join(char_arr)

    def decode(self, s: str) -> List[str]:
        counter = 0
        word_arr = []
        while counter < len(s):
           found_index = s.find("#", counter)
           length = int(s[counter: found_index])
           counter = found_index + 1
           word = s[counter : counter + length]
           word_arr.append(word)
           counter += length
        return word_arr
