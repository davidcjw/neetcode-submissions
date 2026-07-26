class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(paren: str, stack: List[str]):
            if len(paren) == 2*n:
                if not stack:
                    res.append(paren)
                return
             
            stack.append("(")
            dfs(paren+"(", stack)
            stack.pop()  # remove last added

            if stack:
                stack.pop()  # remove corresponding "("
                dfs(paren+")", stack)
                stack.append("(")  # add back to continue backtracking
        
        dfs("", [])
        return res