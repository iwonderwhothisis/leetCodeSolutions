class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        count = 0



        # Skip trailing spaces
        i = length - 1

        while i >= 0 and s[i] == " ":

            i -= 1

        # Count characters in the last word
        while i >= 0 and s[i] != " ":
            count += 1
            i -= 1


        return count


def main():
    solution = Solution()
    result = solution.lengthOfLastWord("this is a test  ")



if __name__ == "__main__":
    main()
