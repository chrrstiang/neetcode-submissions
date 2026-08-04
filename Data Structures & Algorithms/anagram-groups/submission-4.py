class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for s in strs:
            sort = str(sorted(s))
            if not hashMap.get(sort, 0):
                hashMap[sort] = [s]
            else:
                hashMap[sort].append(s)
        
        return list(hashMap.values())