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
        print(s)
        counter = 0
        word_arr = []
        length = []
        while counter < len(s):
            letter = s[counter]
            length.append(letter)
            counter += 1
            if s[counter] == "#":
                length_str = "".join(length)
                length_num = int(length_str)
                print(length_num)
                word = []
                counter += 1
                max_length = counter + length_num
                while counter < max_length:
                    print(counter)
                    letter = s[counter]
                    word.append(letter)
                    counter += 1
                word_arr.append("".join(word))
                length = []
        return word_arr
