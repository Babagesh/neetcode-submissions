class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            "[" : "]",
            "{" : "}",
            "(" : ")"
        }
        stack = []
        for char in s:
            if char in pairs:
                stack.append(char)
            else:
                if stack:
                    opening = stack.pop()
                    if pairs[opening] == char:
                        continue
                    else:
                        return False
                else:
                    return False
        return len(stack) == 0