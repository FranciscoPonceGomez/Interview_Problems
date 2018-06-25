import java.lang.*;

class Solution {
    public static String spiralOrder(int[][] matrix) {
        int t = 0;
        int b = matrix.length-1;
        int l = 0;
        int r = matrix[0].length-1;
        int dir = 0;
        StringBuilder result = new StringBuilder();

        while (t <= b && l <= r)
        {
            if (dir == 0)
            {
                for (int i = l; i <= r; i++)
                {
                    result.append(matrix[t][i]);
                    result.append(',');
                }
                t++;
            }
            else if (dir == 1)
            {
                for (int i = t; i <= b; i++)
                {
                    result.append(matrix[i][r]);
                    result.append(',');
                }
                r--;
            }
            else if (dir == 2)
            {
                for (int i = r; i >= l; i--)
                {
                    result.append(matrix[b][i]);
                    result.append(',');
                }
                b--;
            }
            else if (dir == 3)
            {
                for (int i = b; i >= t; i--)
                {
                    result.append(matrix[i][l]);
                    result.append(',');
                }
                l++;
            }
            dir = (dir+1)%4;
        }
        result.deleteCharAt(result.length()-1);
        return result.toString();
    }

    public static void main (String[] args) 
    {
        int matrix[][] = { {2,  3,  4,  8},
                      {5,  7,  9, 12},
                      {1, 0, 6, 10}
                    };
        System.out.print(spiralOrder(matrix));
    }
}
