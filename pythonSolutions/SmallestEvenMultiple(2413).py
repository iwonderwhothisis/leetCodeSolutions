class Solution(object):
    def smallestEvenMultiple(self, n):

        x = n

        if n % 2 == 0:
            return n

        while x % 2 != 0:
            x = x + n

        return x


def main():
    solution = Solution()  # Create an instance of the Solution class
    result = solution.smallestEvenMultiple(5) # Call the method on the instance
    print(result)


if __name__ == "__main__":
    main()