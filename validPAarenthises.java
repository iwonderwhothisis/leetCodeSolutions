/**
 * 
 * Longest Valid Parentheses
 * 
 *  Given a string containing just the characters 
 * '(' and ')', return the length of the longest
 *  valid (well-formed) parentheses substring
 */


 class Solution {
    public int longestValidParentheses(String s) {

        int maxans = 0;
        Stack<Integer> stack = new Stack<>();
        stack.push(-1);

        for (int i = 0; i < s.length(); i++) {              //For each character in the string, 
            if (s.charAt(i) == '(') {                       //if it is a left parenthesis, 
                stack.push(i);                              //push its index to the stack.
            } else {
                stack.pop();                                //else, pop the top element and subtract the current element's index from the top element of the stack, 
                
                if (stack.empty()) {                        //If stack becomes empty, push the current element's index onto the stack. 
                    stack.push(i);
                } else {
                    maxans = Math.max(maxans, i - stack.peek());        //
                }
            }
        }
        return maxans;
    }
}
