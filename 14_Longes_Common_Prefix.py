class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ""

        shortest_str_index = 0

        if len(strs) == 0:
            return common_prefix
        
        if len(strs) == 1:
            if len(strs[0]) > 0:
                return strs[0][0]
            else:
                common_prefix

        for i, str in enumerate(strs):
            
            if len(str) > len(strs[shortest_str_index]):
                shortest_str_index = i

        for i in range(len(strs[shortest_str_index])):
            char_list = []
            for str in strs:
                if i >= len(str):
                    return common_prefix
                if str != '':
                    char_list.append(str[i])
                    # break
                else:
                    return common_prefix
            
            if len(set(char_list)) == 1:
                common_prefix = "".join([common_prefix, char_list[0]])
            else:
                return common_prefix
            
        return common_prefix


            


if __name__ == '__main__':
    s = Solution()
    # assert s.longestCommonPrefix(strs = ["flower","flow","flight"]) == "fl"
    # assert s.longestCommonPrefix(strs = ["dog","racecar","car"]) == ""
    # assert s.longestCommonPrefix(strs = ["","cbc","c","ca"]) == ""
    # assert s.longestCommonPrefix(strs = ["","cbc","c","ca"]) == ""
    # assert s.longestCommonPrefix(strs = ["cir","car"]) == "c"
    assert s.longestCommonPrefix(strs = ["ab", "a"]) == "c"