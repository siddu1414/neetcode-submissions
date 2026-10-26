class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans={}
        for s in strs:
            #create a canonical key
            key = "".join(sorted(s))
            if key not in ans:
                ans[key] = []
            ans[key].append(s)
        return list(ans.values())
        