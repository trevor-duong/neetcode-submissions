class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # calculate a frequency tuple for each str in strs. appending string to a dict depending on its frequency tuple. Convert the dict to a list
        anagrams = defaultdict(list)
        for str in strs:
            freq = [0] * 26
            for char in str:
                freq[ord(char) - ord('a')] += 1
            freqTuple = tuple(freq)
            anagrams[freqTuple].append(str)
        
        soln = []
        for i, key in enumerate(anagrams):
            group = []
            for str in anagrams[key]:
                group.append(str)
            soln.append(group)
        
        return soln