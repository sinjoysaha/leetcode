# Solution 1: Using recursion - stack memory during recursive function call

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        def backtrack(o, c):
            if o==c==n:
                res.append(''.join(stack))

            if o<n:
                stack.append('(')
                backtrack(o+1, c)
                stack.pop()
            if c<o:
                stack.append(')')
                backtrack(o, c+1)
                stack.pop()

        backtrack(0, 0)
        return res
    
# Solution 2: Using stack of dicts to keep track of no. of open and close brackets
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = [{'f':True, 'o':1, 'c':0, 's':'('}]
        res = []
        for i in range(0, (2**(2*n))-2):
            if not stack[i]['f']:
                stack.append({'f':False})
                stack.append({'f':False})
                continue

            o = stack[i]['o']
            c = stack[i]['c']
            s = stack[i]['s']
            if o==n:
                stack.append({'f':False})
            else:
                stack.append({'f':True, 'o': o+1, 'c':c, 's':s+'('})
            if c==o:
                stack.append({'f':False})
            else:
                stack.append({'f':True, 'o': o, 'c':c+1, 's':s+')'})
                if o==n and (c+1)==n:
                    res.append(s+')')

        return res