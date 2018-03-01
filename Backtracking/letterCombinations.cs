using System;
using System.Collections.Generic;
using System.Text;

namespace InterviewProblemsTests
{
    class Program
    {
        private Dictionary<char, List<char>> phonenumber = new Dictionary<char, List<char>>
        {
            {'0', new List<char>()},
            {'1', new List<char>()},
            {'2', new List<char>() {'a', 'b', 'c'}},
            {'3', new List<char>() {'d', 'e', 'f'}},
            {'4', new List<char>() {'g', 'h', 'i'}},
            {'5', new List<char>() {'j', 'k', 'l'}},
            {'6', new List<char>() {'m', 'n', 'o'}},
            {'7', new List<char>() {'p', 'q', 'r', 's'}},
            {'8', new List<char>() {'t', 'u', 'v'}},
            {'9', new List<char>() {'w', 'x', 'y', 'z'}}
        };
        private List<string> resstring = new List<string>();

        static void Main(string[] args)
        {
            Program p = new Program();
            Program q = new Program();

            p.LetterCombinations("23");
            q.LetterCombinations2("23");
        }


        public IList<string> LetterCombinations(string digits)
        {
            LetterCombinationsHelper(digits, 0, new StringBuilder());

            return resstring;
        }

        private void LetterCombinationsHelper(string digits, int i, StringBuilder result)
        {
            if (i >= digits.Length)
            {
                if (result.Length > 0)
                {
                    resstring.Add(result.ToString());
                }
                return;
            }

            var cur = phonenumber[digits[i]];
            foreach (var letter in cur)
            {
                result.Append(letter);
                LetterCombinationsHelper(digits, i + 1, result);
                result.Remove(result.Length - 1, 1);
            }
        }

        public IList<string> LetterCombinations2(string digits)
        {
            if (string.IsNullOrEmpty(digits)) { return new List<string>(); }
            var ans = new List<string>() { "" };
            var mapping = new[] { "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz" };

            foreach (char digit in digits)
            {
                var backup = new List<string>();
                foreach (var ch in mapping[digit - '0'])
                {
                    foreach (var answer in ans)
                    {
                        backup.Add(answer + ch);
                    }
                }

                ans = backup;
            }
            return ans;
        }
    }
}
