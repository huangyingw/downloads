public class Solution extends Reader4
{

    public int read(char[] buf, int n)
    {
        char[] buffer = new char[4];
        int oneRead = 0;
        int offset = 0;
        boolean lessthan4 = false;
        int haveRead = 0;

        while (!lessthan4 && haveRead < n)
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

