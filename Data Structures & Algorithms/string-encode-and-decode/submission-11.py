class Solution:

    def encode(self, strs: List[str]) -> str:
        parts = []
        for string in strs:
            parts.append(str(len(string)) + '#' + string)
        encoded = "".join(parts)
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        soln = []
        i = 0
        length = -1
        while i < len(s):
            # parse length
            if length == -1:
                digits = []
                while i < len(s) and s[i].isdigit():
                    digits.append(s[i])
                    i += 1
                if digits:
                    length = int("".join(digits))

            print(length)
            if i < len(s) and s[i] == '#' and length != -1:
                i += 1
                soln.append(s[i: i+length])
                i = i + length
                length = -1


            
        return soln
