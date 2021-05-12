public class Solution {
    public boolean validTree(int n, int[][] edges) {
        UnionFind uf = new UnionFind(n);
        for(int i = 0; i < edges.length; i++){
            // 如果两个节点已经在同一集合中，说明新的边将产生环路
            if(!uf.union(edges[i][0], edges[i][1])){
                return false;
            }
        }
        return uf.count() == 1;
    }
    
    public class UnionFind {
        
        int[] ids;
        int cnt;
        
        public UnionFind(int size){
            this.ids = new int[size];
            //初始化并查集，每个节点对应自己的集合号
            for(int i = 0; i < this.ids.length; i++){
                this.ids[i] = i;
            }
            this.cnt = size;
        }
        public boolean union(int m, int n){
            int src = find(m);
            int dst = find(n);
            //如果两个节点不在同一集合中，将两个集合合并为一个
            if(src != dst){
                for(int i = 0; i < ids.length; i++){
                    if(ids[i] == src){
                        ids[i] = dst;
                    }
                }
                // 合并完集合后，集合数减一
                cnt--;
                return true;
            } else {
                return false;
            }
        }
        public int find(int m){
            return ids[m];
        }
        public boolean areConnected(int m, int n){
            return find(m) == find(n);
        }
        public int count(){
            return cnt;
        }
    }
}
