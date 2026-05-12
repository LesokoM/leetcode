class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ""

        counter = 0 
        while counter < 2:
            for i in range(0, len(strs)-1):
                if strs[i][i] == strs[i+1][i]:
                    if strs[i+1][i] == strs[-1][i]:
                        counter += 1
                        common+=strs[i][i]
                else: 
                    return ""
        return common

sol = Solution()
sol.longestCommonPrefix(["dog","racecar","car"])
            