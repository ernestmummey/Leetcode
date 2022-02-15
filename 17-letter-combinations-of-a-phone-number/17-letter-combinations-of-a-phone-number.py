class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = { "2": "abc",
                        "3": "def",
                        "4": "ghi",
                        "5": "jkl",
                        "6": "mno",
                        "7": "qprs",
                        "8": "tuv",
                        "9": "wxyz" }
        
        def backtracking(i, current_str):
            if len(current_str) == len(digits):
                res.append(current_str)
                return
            
            for c in digitToChar[digits[i]]:
                backtracking(i + 1, current_str + c)
                
        if digits:
            backtracking(0,"")  
        return res
                
            