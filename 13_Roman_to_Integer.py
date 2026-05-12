class Solution:
    def romanToInt(self, s: str) -> int:
        
        roman_numerical = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        number = 0

        for i, char in enumerate(s):
            
            if i + 1 < len(s):
                if roman_numerical[s[i]] >= roman_numerical[s[i + 1]]:
                    number += roman_numerical[char]
                    continue
                else:
                    number -= roman_numerical[char]
            else:
                number += roman_numerical[char]

        return number
        


if __name__ == '__main__':
    solution = Solution()
    assert solution.romanToInt("III") == 3
    assert solution.romanToInt("LVIII") == 58
    assert solution.romanToInt("MCMXCIV") == 1994