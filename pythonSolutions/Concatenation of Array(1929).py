class Solution(object):
    def getConcatenation(self, nums):

        length = len(nums)
        for i in range(length):
            nums.append(nums[i])
        return nums

def main():
    solution = Solution()  # Create an instance of the Solution class
    nums = [2, 3, 4, 5]
    print(solution.getConcatenation(nums))


if __name__ == "__main__":
    main()