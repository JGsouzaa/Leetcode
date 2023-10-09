class Solution {
    public int romanToInt(String s) {
        HashMap<Character, Integer> map = new HashMap<>();
        map.put('I', 1);
        map.put('V', 5);
        map.put('X', 10);
        map.put('L', 50);
        map.put('C', 100);
        map.put('D', 500);
        map.put('M', 1000);
        
        int eBefore = 0;
        int resp = 0;

        for (int i = 0; i< s.length(); i++){
            if (i == 0){
                eBefore = s.charAt(i);
                resp += map.get(s.charAt(i));
            } else {
                if ((s.charAt(i) == 'V' || s.charAt(i) == 'X') && (eBefore == 'I')){
                    resp += (map.get(s.charAt(i)) - 2);
                } else if ((s.charAt(i) == 'L' || s.charAt(i) == 'C') && (eBefore == 'X')) {
                    resp += (map.get(s.charAt(i)) - 20);
                } else if ((s.charAt(i) == 'D' || s.charAt(i) == 'M') && (eBefore == 'C')) {
                    resp += (map.get(s.charAt(i)) - 200);
                } else {
                    resp += map.get(s.charAt(i));
                }
                eBefore = s.charAt(i);
            }
        }
        return resp;
    }
}