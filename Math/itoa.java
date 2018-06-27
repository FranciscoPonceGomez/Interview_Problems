class Solution {
    // We have different options to handle negative numbers, I am going to consider returning
    // the converted number with a '-' prefix
    // ---Time complexity---: O(n), n = number of digits in the input 
    // ---Space complexity---: O(n), n = number of digits in the input
    public static final int MAX_SIZE = 32;
  
    public static String itoa(int value, int base) {
        if (base != 2 && base != 8 && base != 16) 
          throw new IllegalArgumentException("Error. Only binary (2), octal(8) and hexadecimal(16) bases are allowed");
      	
      	char[] res = new char[MAX_SIZE];
        int tmp = value;
      	int i = 0;
        while (tmp > 0) {
            res[i] = toChar(tmp % base);
            tmp = tmp / base;
          	i++;
        }
        if (tmp < 0)
            return '-' + itoa(-value,base);
        return reverse(res,i);
    }

    // For bases larger than 10, this method encode the digits into ASCII ISO 266
    // I am assuming that we are allowed to use built in data type casting like (char). If that is not the case,
    // we can add:
    //Map<String, String> alphabet = new HashMap<String, String>();
    //for(int i = 0; i < 16; i++) {
    //    i > 10 ? map.put(i.toString(),i.toString()) : map.put(i, i+'A');
    //}
    // which is equivalent to:
    // alphabet = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    // return alphabet[value]
    // We can add more elements to our alphabet for bases larget than 16
    public static char toChar(int value) {
        return (value < 10 && value >= 0) ? (char)(value + '0') : (char)(value - 10 + 'A');
    }

    // Since we are trying to limit the use of built-in functions, one of the best ways to reverse arrays is by using two indexes
    // ---Time Complexity---: O(n/2) ~= O(n), n = number of digits in the input 
    // This method doesn't increase the total complexity if itoa since O(2n) ~= O(n)
    // ---Space Complexity---: O(1)
    public static String reverse(char[] value, int length) {
        int i = 0;
        int j = length-1;
        char tmp;
        while (i <= j) {
            tmp = value[i];
            value[i] = value[j];
            value[j] = tmp;
            i++;
          	j--;
        }
     	return new String(value);
    } 

    public static void main (String[] args) {
        int value = -123456;
        System.out.print(itoa(value, 2));
    }
}