public class SnakeGame {  
    private Set<String> board = new HashSet<>();  
    private int[][] food;  
    private int eat = 0;  
    private LinkedList<Position> snake = new LinkedList<>();  
    private int width, height;  
      
    private boolean eat(int y, int x) {  
        if (eat >= food.length) return false;  
        if (food[eat][0] < 0 || food[eat][0] >= height || food[eat][1] < 0 || food[eat][1] >= width) return false;  
        if (y == food[eat][0] && x == food[eat][1]) return true;  
        return false;  
    }  
  
    /** Initialize your data structure here. 
        @param width - screen width 
        @param height - screen height  
        @param food - A list of food positions 
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0]. */  
    public SnakeGame(int width, int height, int[][] food) {  
        this.food = food;  
        Position head = new Position(0,0);  
        this.snake.add(head);  
        board.add(head.toString());  
        this.height = height;  
        this.width = width;  
    }  
      
    /** Moves the snake. 
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down  
        @return The game's score after the move. Return -1 if game over.  
        Game over when snake crosses the screen boundary or bites its body. */  
    public int move(String direction) {  
        Position head = snake.getFirst();  
        Position next = new Position(head.y, head.x);  
        if ("U".equals(direction)) {  
            next.y --;  
        } else if ("D".equals(direction)) {  
            next.y ++;  
        } else if ("L".equals(direction)) {  
            next.x --;  
        } else if ("R".equals(direction)) {  
            next.x ++;  
        } else {  
            return -1;  
        }  
        if (next.y < 0 || next.y >= height || next.x < 0 || next.x >= width) return -1;  
        String ns = next.toString();  
        if (eat(next.y, next.x)) {  
            snake.addFirst(next);  
            board.add(ns);  
            return ++ eat;  
        }  
        Position tail = snake.getLast();  
        board.remove(tail.toString());  
        snake.removeLast();  
        if (board.contains(ns)) return -1;  
        snake.addFirst(next);  
        board.add(ns);  
        return eat;  
    }  
}  
class Position {  
    int y, x;  
    Position(int y, int x) {  
        this.y = y;  
        this.x = x;  
    }  
    public String toString() {  
        return y + "," + x;  
    }  
} 

