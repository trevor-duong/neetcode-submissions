class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {} # map of Key (string) : Value (List[string])
        soln = [] # return val
        for i in range(len(strs)): # O(n)
            sortedString = ''.join(sorted(strs[i])) # O(klogk)
            if sortedString not in map: 
                map[sortedString] = [] 
            map[sortedString].append(strs[i])
        for key, values in map.items(): # O(n)
            group = []
            for string in values:
                group.append(string)
            soln.append(group)
        #total runtime is (O(n * klogk)) where n is len(strs) and k is the avg length of each string
        return soln