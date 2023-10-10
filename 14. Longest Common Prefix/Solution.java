class Solution {
		public String longestCommonPrefix(String[] strs) {
				
			Arrays.sort(strs);
			for (int j = 0; j< strs.length; j++) {
				strs[j] = strs[j].toLowerCase();
			}
			
			String first_word = strs[0];
			String last_word = strs[strs.length - 1];		    	
			int length_of_prefix = 0;
			
			while(length_of_prefix < first_word.length()) {
				
				if (first_word.charAt(length_of_prefix) == last_word.charAt(length_of_prefix)) {
					length_of_prefix++;	
				} else {
					break;
				}		    		
			}
		return (first_word.substring(0, length_of_prefix));
		}
}