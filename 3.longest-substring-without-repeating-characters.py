#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
class Solution:
    def lengthOfLongestSubstring(self, s):
        st = {}
        i,ans = 0 0
        for j in range(len(s)):
            if s[j] in st:
                i = max(st[s[j]],i)
            ans = max(ans,j -i +1 )
            st[s[j]] = j +1
        return ans;
        

