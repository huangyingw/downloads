class MyQueue
{

    Stack<Integer> input = new Stack();
    Stack<Integer> output = new Stack();

    public void push(int x)
    {
        input.push(x);
    }

    public int pop()
    {
        peek();
        return output.pop();
    }

    public int peek()
    {
        return output.peek();
    }

    public boolean empty()
    {
        return input.empty() && output.empty();
    }
}
