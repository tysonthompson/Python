class Solution:
    def firstUniqChar(self, s: str) -> int:
        alphabet = {}
        indecies = {}
        count = 0
        for character in s:
            if character not in alphabet:
                alphabet[character]=1
            else:
                alphabet[character]=alphabet[character]+1
            indecies[character]=count
            count+=1
        for letter in alphabet:
            if alphabet[letter] == 1:
                return indecies[letter]
            
        return -1
