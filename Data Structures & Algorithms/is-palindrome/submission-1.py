class Solution:
    def isPalindrome(self, s: str) -> bool:
        s="".join([char.lower() for char in s if char.isalnum()])
        #to remove spaces and convert cases, use ".join(s.split()).lower(), use isalnum for getting only the numerical and alphabets
        l=s[::-1]
        if l==s:
            return True
        else:
            return False