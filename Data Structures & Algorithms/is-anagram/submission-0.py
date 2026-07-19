class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False;

        mapS, mapT = {}, {}

        # build hash maps to compare
        for i in range(len(s)):
            # assign/increment key of letter for s string
            mapS[s[i]] = 1 + mapS.get(s[i], 0);
            # assign/increment key of letter for t string
            mapT[t[i]] = 1 + mapT.get(t[i], 0);

        # are the maps equal? same keys and values
        return mapS == mapT;
