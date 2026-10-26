class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        r=0
        if len(s)==len(t):
            t_list = list(t)
            for i in range(len(s)):
                for j in range(len(t_list)):
                    if s[i]==t_list[j]:
                        r+=1
                        t_list.pop(j)
                        break
                    
            
        return len(s)==r and len(s) > 0 or s == t