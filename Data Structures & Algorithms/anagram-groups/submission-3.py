class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        agms = {}

        for s in strs:
            if "".join(sorted(s)) in agms:
                agms["".join(sorted(s))].append(s)
            else:
                agms["".join(sorted(s))] = [s]

        result = []
        for key, value in agms.items():
            result.append(value)
        return result
        