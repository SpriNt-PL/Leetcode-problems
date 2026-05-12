class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        print(x_str)
        left = ''
        right = ''
        if len(x_str) % 2 == 0:
            for i, char in enumerate(x_str):
                if i < len(x_str) / 2:
                    left = ''.join([left, char])
                else:
                    right = ''.join([right, char])

            if (left == right[::-1]):
                return True
            else:
                return False
            
        else:
            for i, char in enumerate(x_str):
                if i < len(x_str) / 2 - 1:
                    left = ''.join([left, char])
                
                elif i == len(x_str) // 2:
                    continue
                else:
                    right = ''.join([right, char])

            if (left == right[::-1]):
                return True
            else:
                return False
        

                



if __name__ == '__main__':
    solution = Solution()
    assert solution.isPalindrome(1221) == True
    assert solution.isPalindrome(121) == True
    assert solution.isPalindrome(123) == False