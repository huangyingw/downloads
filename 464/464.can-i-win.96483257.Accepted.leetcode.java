public class Solution
{
    public boolean canIWin(int maxChoosableInteger, int desiredTotal)
    {
        if (desiredTotal <= 0)
        {
            return true;
        }

        //如果1到最大能选的值所有和都不能满足目标值，那么肯定失败
        if (maxChoosableInteger * (maxChoosableInteger + 1) / 2 < desiredTotal)
        {
            return false;
        }

        char state[] = new char[maxChoosableInteger];

        for (int i = 0; i < maxChoosableInteger; i++)
        {
            state[i] = '0';
        }

        return dfs(desiredTotal, state, new HashMap<>());
    }
    private boolean dfs(int total, char[] state, HashMap<String, Boolean> hashMap)
    {
        String key = new String(state);

        if (hashMap.containsKey(key))
        {
            return hashMap.get(key);
        }

        for (int i = 0; i < state.length; i++)
        {
            if (state[i] == '0')
            {
                state[i] = '1';

                if (total <= i + 1 || !dfs(total - (i + 1), state, hashMap))
                {
                    hashMap.put(key, true);
                    state[i] = '0';
                    return true;
                }

                state[i] = '0';
            }
        }

        hashMap.put(key, false);
        return false;
    }


}
