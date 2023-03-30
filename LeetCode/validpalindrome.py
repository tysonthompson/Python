class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        ns = ""
        for character in s:
            if character.isalnum():
                ns+=character
        if ns == ns[::-1]:
            return True
        else:
            return False
