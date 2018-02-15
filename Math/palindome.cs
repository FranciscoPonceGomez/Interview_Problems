//Determine whether an integer is a palindrome. Do this without extra space.

//A palindrome integer is an integer x for which reverse(x) = x where reverse(x) is x with its digit reversed.
//Negative numbers are not palindromic.

//Example :

//Input : 12121
//Output : True

//Input : 123
//Output : False

public class Solution {
	public boolean isPalindrome(int a) {
	    if(a == check(a))
	        return true;
	    else
	        return false;
	}
	
	public int check(int num){
        int reverted = 0;
        while (num > 0) {
            reverted = reverted*10 + num%10;
            num /= 10;
        }
      return reverted;
	}
}
// 32123 3212 3 i = 0
// 3212 321 2   i = 1
// 321 32 1     i = 2
// 1*10exp0 + 2*10exp1 + 3*10exp2
