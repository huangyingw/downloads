public class HitCounter {
    private ArrayDeque<Integer> memory;
    /** Initialize your data structure here. */
    public HitCounter() {
        memory = new ArrayDeque<>();
    }
 
    /** Record a hit.
        @param timestamp - The current timestamp (in seconds granularity). */
    public void hit(int timestamp) {
        memory.add(timestamp);
        // int top = memory.poll();
        // while (timestamp - top >= 300) {
        //     top = memory.poll();
        // }
        // memory.addFirst(top);
    }
 
    /** Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity). */
    public int getHits(int timestamp) {
        if (!memory.isEmpty()) {
            while (!memory.isEmpty() && (timestamp - memory.peek()) >= 300) {
                memory.poll();
            }
        }
        return memory.size();
    }
}
 
/**
 * Your HitCounter object will be instantiated and called as such:
 * HitCounter obj = new HitCounter();
 * obj.hit(timestamp);
 * int param_2 = obj.getHits(timestamp);
 */
