public class Solution {
 public int lastRemaining(int n) {
	boolean left = true;
	int remain = n;
	int step = 1;
	int head = 1;
	while(remain>1){
		if(left||remain%2==1){
			head +=step;
			
		}
		remain /=2;
		left =!left;
		step *=2;
	}
	return head;
}
}
