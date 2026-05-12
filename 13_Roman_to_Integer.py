class Solution:
    def romanToInt(self, s: str) -> int:
        number = 0
        if len(s) == 0:
            return number

        for i, char in enumerate(s):
            if char == "I":
                if i - 1 == len(s):
                    if s[i + 1] == "V":
                        number += 4
                        continue
                    elif s[i + 1] == "X":
                        number += 9
                        continue
                number += 1


        return number


if __name__ == '__main__':
    solution = Solution()
    assert solution.romanToInt("III") == 3
    assert solution.romanToInt("LVIII") == 58
    assert solution.romanToInt("MCMXCIV") == 1994