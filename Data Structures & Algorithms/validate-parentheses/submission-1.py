class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            "(": ")",
            "{": "}",
            "[": "]",
        }
        for i in s:
            if i in mapping.keys():
                stack.append(i)
            else:
                # closing bracket but nothing to match against
                if len(stack) == 0:
                    return False
                opp = stack.pop()
                if mapping[opp] != i:
                    return False
                
        return len(stack) == 0