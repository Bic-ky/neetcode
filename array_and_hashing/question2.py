# Valid Anagram

# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.


class Solution:
    def isAnagram(self, s: str , t: str) -> bool :
        
        first_str = "".join(sorted(s))
        second_str = "".join(sorted(t))

        if first_str == second_str :
            return True
        else:    
            return False
    

if __name__ == "__main__":
    sol = Solution()
    s="racecar"
    t="carrace"
    res = sol.isAnagram(s,t)

    print("The word is anagram? >>" , res)