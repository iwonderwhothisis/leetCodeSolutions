class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        result = True
        holder = []
        found = False
        for x in s:
            if x == "(" or x == "[" or x == "{":
               holder.append(x)
            else:
                if x == ")" or x =="]" or x == "}":
                    for i in holder:
                        if x == ")" and i == "(":
                            holder.remove("(")
                            found = True
                        else:
                            if x == "]" and i == "[":
                                holder.remove("[")
                                found = True
                            else:
                                if x == "}" and i == "{":
                                    holder.remove("{")
                                    found = True
                    if found == False:
                        print("Parentheses invalid")
                        return False


        if len(holder) == 0:
            print("Parentheses valid")
            return True
        else:
            print("Parentheses invalid")
            return False



def main():
   mySoloution = Solution()
   mySoloution.isValid("([)]")




if __name__ == "__main__":
    main()


