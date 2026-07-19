class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for s in strs:
            count = [0] * 26 # make list with 26 arrays
            for c in s:
                # use unicode to access index of letter
                count[ord(c) - ord('a')] += 1
            # add string to list with the corresponding tuple key
            result[tuple(count)].append(s)

        return list(result.values())