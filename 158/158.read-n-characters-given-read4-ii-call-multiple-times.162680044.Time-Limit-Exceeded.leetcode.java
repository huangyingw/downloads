public class Solution extends Reader4
{
    private char[] buffer = new char[4];
    private int oneRead = 0;
    private int offset = 0;

    public int read(char[] buf, int n)
    {
        boolean lessthan4 = false;
        int haveRead = 0;

        while (!lessthan4)
        {
            if (oneRead == 0)
            {
                oneRead = read4(buffer);
                lessthan4 = oneRead < 4;
            }

            int actRead = Math.min(n - haveRead, oneRead);

            for (int i = 0; i < actRead; i++)
            {
                buf[haveRead + i] = buffer[offset + i];
            }

            oneRead -= actRead;
            offset = (offset + actRead) % 4;
            haveRead += actRead;
        }

        return haveRead;
    }
}

