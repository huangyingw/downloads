	public class Solution {
		public int lengthOfLastWord(String s) {
			String trimmed = s.trim();
			String[] splitted = trimmed.split("\\s+");
			return splitted[splitted.length - 1].length();
		}
	}

