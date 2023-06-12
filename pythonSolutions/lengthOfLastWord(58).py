class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        index = 0
        space_index = 0
        length = len(s)
        count = 0

        for x in s:  # loops through the whole string
            if x == " ":  # if char is a space, set space index to current index
                space_index = index

            index += 1  # increment index

        # if there are spaces in the string, count how many characters are in the final word
        if space_index != 0:
            if space_index == length - 1:
                return self.reverseWordCount(s)

            index = space_index + 1
            while index < length:
                count += 1
                index += 1
        # if there are no spaces, then return length of the whole string
        elif space_index == 0 and length > 0:
            count = length

        return count

    def reverseWordCount(self, s):
        length = len(s)
        index = 0
        penultimate_space = 0
        word_length = 0

        while index < length:
            if s[index] == " ":
                penultimate_space = index
            index += 1

        count = length - penultimate_space - 1

        return count


def main():
    solution = Solution()  # Create an instance of the Solution class
    result = solution.lengthOfLastWord("this is a test  ")  # Call the method on the instance
    print(result)


if __name__ == "__main__":
    main()
