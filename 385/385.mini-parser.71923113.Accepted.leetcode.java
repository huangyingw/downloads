/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * public interface NestedInteger {
 *     // Constructor initializes an empty nested list.
 *     public NestedInteger();
 *
 *     // Constructor initializes a single integer.
 *     public NestedInteger(int value);
 *
 *     // @return true if this NestedInteger holds a single integer, rather than a nested list.
 *     public boolean isInteger();
 *
 *     // @return the single integer that this NestedInteger holds, if it holds a single integer
 *     // Return null if this NestedInteger holds a nested list
 *     public Integer getInteger();
 *
 *     // Set this NestedInteger to hold a single integer.
 *     public void setInteger(int value);
 *
 *     // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 *     public void add(NestedInteger ni);
 *
 *     // @return the nested list that this NestedInteger holds, if it holds a nested list
 *     // Return null if this NestedInteger holds a single integer
 *     public List<NestedInteger> getList();
 * }
 */
public class Solution {
    public NestedInteger deserialize(String s) {
 
    Stack<NestedInteger> stack = new Stack<NestedInteger>();
    String temp = "";
 
    for(char c: s.toCharArray()){
        switch(c){
            case '[':
                stack.push(new NestedInteger()); //start a new NI
                break;
 
            case ']':
                if(!temp.equals("")){
                    stack.peek().add(new NestedInteger(Integer.parseInt(temp))); //add NI to parent
                    temp="";
                }
 
                NestedInteger top = stack.pop();
                if(!stack.empty()){
                    stack.peek().add(top);
                }else{
                    return top;
                }
 
                break;
 
            case ',':
                if(!temp.equals("")){
                    stack.peek().add(new NestedInteger(Integer.parseInt(temp)));//add NI to parent
                    temp="";
                }
 
                break;
 
            default:
                temp += c;
        }
    }
 
    if(!temp.equals("")){
        return new NestedInteger(Integer.parseInt(temp));
    }
 
    return null;
}
}
