class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openingSet = set(["(", "{", "["])
        mapping = {
            "}": "{",
            "]": "[",
            ")": "(",
        }

        for char in s:
            if char in openingSet:
                stack.append(char)
            else:
                if not stack or mapping[char] != stack[-1]:
                    return False
                
                stack.pop()
            
        return len(stack) == 0
