class Solution:
    def isPalindrome(self, x: int) -> bool:
        convstring = str(x)
        reverse = convstring[::-1]
        return reverse == convstring
