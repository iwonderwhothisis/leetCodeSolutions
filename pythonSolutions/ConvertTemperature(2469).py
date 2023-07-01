class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """

        kelvin = celsius + 273.15
        fahrenheit = celsius * 1.80 + 32.00

        result = [kelvin, fahrenheit]

        return result


def main():
    solution = Solution()  # Create an instance of the Solution class
    results = solution.convertTemperature(44) # Call the method on the instance
    print(results)


if __name__ == "__main__":
    main()