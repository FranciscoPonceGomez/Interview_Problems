using System;
using System.Collections.Generic;

namespace InterviewProblemsTests
{
    class Program
    {
        static void Main(string[] args)
        {
            GetCombination(new List<object> { 3,'B',2,'C',6,'F'});
        }

        static void GetCombination<T>(List<T> list)
        {
            double count = Math.Pow(2, list.Count);
            for (int i = 1; i <= count - 1; i++)
            {
                // convert to binary with list.Count length
                string str = Convert.ToString(i, 2).PadLeft(list.Count, '0');
                for (int j = 0; j < str.Length; j++)
                {
                    if (str[j] == '1')
                    {
                        Console.Write(list[j]);
                    }
                }
                Console.WriteLine();
            }
        }
    }
}

