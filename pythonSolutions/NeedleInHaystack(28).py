class Solution(object):
    def strStr(self, haystack, needle):


        for x in haystack:
            print(x)
            if needle[0] == x:
                stack_index = haystack.index(x)
                needle_index = 0
                found = True
                for y in needle:
                    if needle[needle_index] != haystack[stack_index]:
                        found = False
                    else:
                        stack_index + 1
                        needle_index + 1





def main():
    mySolution = Solution()
    result = mySolution.strStr("this is an example", "an")
    print(result)


if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()
