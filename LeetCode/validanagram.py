class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        charCounts = {}
        for character in s:
            if character in charCounts:
                charCounts[character] = charCounts[character]+1
            else:
                charCounts[character] = 1
        
        for character in t:
            if character in charCounts:
                charCounts[character] = charCounts[character]-1
            else:
                return False
            if charCounts[character] < 0:
                return False
        
        for character in charCounts:
            if charCounts[character] >0:
                return False
        return True
