class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        def stringint(self):
            if x < 0:
                return False
            if x == 0:
                return True
            pali = str(x)
            lenpali = len(x)
            n = lenpali - 1
            for x in range(len(pali)):
                x = 1