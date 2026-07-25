class Solution:

    def encode(self, strs: List[str]) -> str:
        if (len(strs) == 0):
            return ""
        string = ""
        for s in strs:
            if (s == ""):
                s = "blank"
            else:
                s = s.encode().hex()
            if (string == ""):
                string = s
            else:
                string = string + " " + s
        return string

    def decode(self, s: str) -> List[str]:
        if (len(s) == 0):
            return []
        arr = s.split(" ")
        for i, word in enumerate(arr):
            if (word == "blank"):
                word = ""
            else:
                word = bytes.fromhex(word).decode('utf-8')
            arr[i] = word
        return arr