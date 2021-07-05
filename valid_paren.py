class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {'(':')','[':']','{':'}'}
        for c in s:
            print("%%%",c)
            if c in match:
                print(c)
                stack.append(c)
                print("***",stack)
            else:
                if not stack or match[stack.pop()]!=c:
                    return False
        return not stack

s = Solution()
print(s.isValid("(){}{["))