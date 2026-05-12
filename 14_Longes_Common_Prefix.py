class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ""

        shortest_str_index = 0
        for i, str in enumerate(strs):
            if i == 0:
                shortest_str_index = 1
            else:
                if len(strs[i - 1]) > len(str):
                    shortest_str_index = i

        if len(strs[shortest_str_index]) == 0:
            return common_prefix

        for i in range(len(strs[shortest_str_index])):
            char_list = []
            for str in strs:
                char_list.append(str[i])
            
            if len(set(char_list)) == 1:
                common_prefix = "".join([common_prefix, char_list[0]])
            else:
                return common_prefix
            
        return common_prefix


            


if __name__ == '__main__':
    s = Solution()
    assert s.longestCommonPrefix(strs = ["flower","flow","flight"]) == "fl"
    assert s.longestCommonPrefix(strs = ["dog","racecar","car"]) == ""