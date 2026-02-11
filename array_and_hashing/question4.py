# Group Anagrams

# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
# 
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

from typing import List

class Solution():
    def groupAnagrams(self , strs : List[str]) -> List[List[str]]:

        anagram_map = {}
        
        for word in strs:
            sorted_word = ''.join(sorted(word))

            print(sorted_word)
            
            if sorted_word not in anagram_map:
                anagram_map[sorted_word] = []

            
            anagram_map[sorted_word].append(word)
            print(anagram_map)
        
        return list(anagram_map.values())




if __name__ == "__main__":

    sol = Solution()

    strs = ["act","pots","tops","cat","stop","hat"]

    res = sol.groupAnagrams(strs)

    print(res)