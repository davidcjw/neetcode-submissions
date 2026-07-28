class Solution:
    def __init__(self):
        self.delimiter = "/"

    def encode(self, strs: List[str]) -> str:
        # 4/ello5/0orld
        res = ""
        for s in strs:
            res += f"{len(s)}{self.delimiter}{s}"
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        currWordLengthStr = ""
        i = 0
        print(s)
        while i < len(s):
            if s[i] == self.delimiter:
                # currWordLength=2
                # i=2; s[3:5]
                res.append(s[i+1:i+int(currWordLengthStr)+1])
                i = i+int(currWordLengthStr)+1
                currWordLengthStr = ""
            else:
                currWordLengthStr += s[i]
                i += 1
        
        return res
