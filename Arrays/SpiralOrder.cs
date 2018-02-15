class Solution {
    public List<int> spiralOrder(List<List<int>> A) {
        int t = 0;
        int b = A.Count-1;
        int l = 0;
        int r = A[0].Count-1;
        int dir = 0;
        List<int> result = new List<int>();

        while (t <= b && l <= r)
        {
            if (dir == 0)
            {
                for (int i = l; i <= r; i++)
                {
                    result.Add(A[t][i]);
                }
                t++;
            }
            else if (dir == 1)
            {
                for (int i = t; i <= b; i++)
                {
                    result.Add(A[i][r]);
                }
                r--;
            }
            else if (dir == 2)
            {
                for (int i = r; i >= l; i--)
                {
                    result.Add(A[b][i]);
                }
                b--;
            }
            else if (dir == 3)
            {
                for (int i = b; i >= t; i--)
                {
                    result.Add(A[i][l]);
                }
                l++;
            }
            dir = (dir+1)%4;
        }
        return result;
    }
}
