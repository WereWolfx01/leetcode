class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ['()'];
        
    def generateParenthesis(self, n):
        def generate(leftnum, rightnum, s, result):
            if leftnum == 0 and rightnum == 0:
                result.append(s)
            if leftnum > 0:
                generate(leftnum - 1, rightnum, s + '(', result)
            if rightnum > 0 and leftnum < rightnum:
                generate(leftnum, rightnum - 1, s + ')', result)
                
        result = []
        s = ''
        generate(n, n, s, result)
        return result
