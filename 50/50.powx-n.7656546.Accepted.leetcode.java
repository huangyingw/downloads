public class Solution {
public double pow(double x, int n) {
	if (n == 0)
		return 1;
	if (n == 1)
		return x;
 
	int pn = n > 0 ? n : -n;// positive n
	int pn2 = pn;
 
	double px = x > 0 ? x : -x;// positive x
	double result = px;
 
	int k = 1;
	//the key part of solving this problem
	while (pn / 2 > 0) {
		result = result * result;
		pn = pn / 2;
		k = k * 2;
	}
 
	result = result * pow(px, pn2 - k);
 
	// handle negative result
	if (x < 0 && n % 2 == 1)
		result = -result;
 
	// handle negative power
	if (n < 0)
		result = 1 / result;
 
	return result;
    }
}
