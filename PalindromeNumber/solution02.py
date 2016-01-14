'''
Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.

Some hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.
'''

#doing the reverse directly into the integer, slower!
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        xx = 0
        newx = x 
        if x>0:
            while x>0:
                xx = xx*10 + x%10
                x/=10
            return xx == newx
        elif x == 0:
            return True
        else:
            return False
        