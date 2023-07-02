class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        temp_str = ''
        #if str2 is bigger than str1
        if len(str2)> len(str1):
            str1,str2= str2,str1
        #switch positions so they hold the others value

        for i in range(len(str2),0,-1):
            temp_str = str2[:i]

            if temp_str * (len(str1)//len(temp_str)) == str1 and temp_str * (len(str2)//len(temp_str)) == str2:
                return temp_str
        return ''

def main():
    mySolution = Solution()
    result = mySolution.gcdOfStrings("ABABABAB", "ABAB")
    print(result)


if __name__ == "__main__":
    main()