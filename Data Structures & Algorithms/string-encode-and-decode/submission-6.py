class Solution:

    def encode(self, strs: List[str]) -> str:
        soln = ""
        if strs == []:
            return ""
        if strs == [""]:
            return "lololol"
        soln = "%@f|".join(strs)
        return soln

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        if s == "lololol":
            return[""]
        split = s.split("%@f|")


        return split