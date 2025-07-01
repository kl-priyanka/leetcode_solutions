class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        n = len(s)
        
        for i in range(0,int(n/2)):
            if ((s[i]) != (s[n-i-1])):
                return False
        return True
