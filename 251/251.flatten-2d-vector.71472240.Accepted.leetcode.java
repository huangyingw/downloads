public class Vector2D implements Iterator<Integer> {

    public Vector2D(List<List<Integer>> vec2d) {  
        row = vec2d.iterator();  
        if(row.hasNext())  
            col = row.next().iterator();  
    } 
    
    @Override
    public Integer next() {
        int lastValue = col.next();  
        return lastValue;  
    }

    @Override
    public boolean hasNext() {
            if(col == null) {  
            return false;  
        }  
        if(col.hasNext()) {  
            return true;  
        } else {  
            while(row.hasNext()) {  
                col = row.next().iterator();  
                if(col.hasNext())  
                    return true;  
            }  
            return false;  
        }  
        
    }
    
    private Iterator<List<Integer>> row = null;  
    private Iterator<Integer> col = null;
}

/**
 * Your Vector2D object will be instantiated and called as such:
 * Vector2D i = new Vector2D(vec2d);
 * while (i.hasNext()) v[f()] = i.next();
 */
