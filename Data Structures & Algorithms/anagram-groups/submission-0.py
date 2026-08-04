class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {} # map of Key (string) : Value (List[string])
        soln = [] # return val
        for i in range(len(strs)): 
            sortedString = ''.join(sorted(strs[i])) 
            if sortedString not in map: # initialize key value if not already
                map[sortedString] = [] 
            map[sortedString].append(strs[i])
        for key, values in map.items():
            group = []
            for string in values:
                group.append(string)
            soln.append(group)
        return soln