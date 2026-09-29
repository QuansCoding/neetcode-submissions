class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = {}
        s2_map = {}

        window_len = len(s1)

        for char in s1:
            s1_map[char] = s1_map.get(char, 0) + 1  # s1 mapping count

        left = 0
        for i, char in enumerate(s2):
            s2_map[char] = s2_map.get(char, 0) + 1

            if i - left + 1 > window_len:
                left_char = s2[left]
                s2_map[left_char] -= 1

                if s2_map[left_char] == 0:  # checks if there is a count for left_char
                    del s2_map[left_char]  # if not removes it

                left += 1  # continue on

            if i - left +  1 == window_len:
                if s1_map == s2_map:
                    return True
        return False