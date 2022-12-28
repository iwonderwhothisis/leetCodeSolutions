//https://leetcode.com/problems/longest-common-prefix/

class Solution {
public:
    //Write a function to find the longest common prefix string amongst an array of strings. 
    //If there is no common prefix, return an empty string "".
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.size() == 0) return "";                                //if the vector is empty, return empty string
        string prefix = strs[0];                                        //set the first string as the prefix
        for (int i = 1; i < strs.size(); i++) {                         //loop through the vector
            while (strs[i].find(prefix) != 0) {                         //if the prefix is not found in the string
                prefix = prefix.substr(0, prefix.length() - 1);         //remove the last character from the prefix
                if (prefix.empty()) return "";                          //if the prefix is empty, return empty string
            }
        }
        return prefix;                                                  //return the prefix           
    }
};