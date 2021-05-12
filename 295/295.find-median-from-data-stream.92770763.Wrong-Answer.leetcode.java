class MedianFinder
{
    PriorityQueue<Integer> maxHeap = new PriorityQueue<Integer>();
    PriorityQueue<Integer> minHeap = new PriorityQueue<Integer>(Collections.reverseOrder());

    public void addNum(int num)
    {
        minHeap.offer(num);
        maxHeap.offer(minHeap.poll());
        
        System.out.println("num --> " + num);
        System.out.println("maxHeap.peek() --> " + maxHeap.peek());
        System.out.println("minHeap.peek() --> " + minHeap.peek());
        
        while (maxHeap.size() > minHeap.size() + 1)
        {
            minHeap.offer(maxHeap.poll());
        }

        print(maxHeap);
        print(minHeap);
    }

    public double findMedian()
    {
        if (maxHeap.size() > minHeap.size())
        {
            return maxHeap.peek();
        }
        else
        {
            return (minHeap.peek() + maxHeap.peek()) / 2;
        }
    }
    
    public void print(PriorityQueue heap)
    {
        Iterator<Integer> iter = heap.iterator();
        
        while (iter.hasNext())
        {
            System.out.print(iter.next() + ",");
        }
        
        System.out.println();
    }
}
