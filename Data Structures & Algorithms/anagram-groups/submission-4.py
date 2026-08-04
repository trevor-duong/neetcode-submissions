class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # CHARACTER FREQUENCY APPROACH SINCE SORTING EACH STRING IS SLOW
        # 1. Iterate through strs
            # Create a frequency table for string in strs
            # Convert the table to a tuple (because it is hashable so can be used as a key in a hashmap)
            # to be put in a hashmap where key is the tuple and value is a list of words
        #2. Iterate through hashmap and convert to List[List[str]]
        frequencyHashMap = {}
        for string in strs: # O(n)
            frequencies = [0] * 26 # Create a list of size 26 
            for char in string: # O(k)
                freqIndex = ord(char) - ord('a')
                frequencies[freqIndex] += 1
            freqAsTuple = tuple(frequencies)
            if freqAsTuple not in frequencyHashMap:
                frequencyHashMap[freqAsTuple] = []
            frequencyHashMap[freqAsTuple].append(string)
        
        return list(frequencyHashMap.values())


        