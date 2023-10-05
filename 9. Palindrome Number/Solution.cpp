class Solution {
public:
    bool isPalindrome(int x) {
        long long xb = x;
        long long reverse = 0;
        if (x < 0) {
            return false;
        }
        do {
            reverse = reverse * 10 + xb % 10;
            xb = xb / 10;

        } while (xb > 0);
        
        return (reverse == x);
    }
};