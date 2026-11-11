class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a.strip('"')
        b = b.strip('"')
        total = int(a, 2) + int(b, 2)
        return bin(total)[2:]

        