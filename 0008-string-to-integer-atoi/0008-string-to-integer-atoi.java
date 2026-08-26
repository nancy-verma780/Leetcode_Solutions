class Solution {
    public int myAtoi(String s) {
        if (s == null || s.length() == 0) return 0;
        
        int i = 0;
        int n = s.length();
        int sign = 1;
        int result = 0;
        
        // 1. Skip leading whitespaces
        while (i < n && s.charAt(i) == ' ') {
            i++;
        }
        
        // 2. Handle sign
        if (i < n && (s.charAt(i) == '+' || s.charAt(i) == '-')) {
            sign = (s.charAt(i) == '-') ? -1 : 1;
            i++;
        }
        
        // 3. Convert digits and check overflow
        while (i < n) {
            char ch = s.charAt(i);
            if (ch < '0' || ch > '9') break; // Stop at non-digit
            
            int digit = ch - '0';
            
            // 4. Overflow Check: 
            // INT_MAX = 2147483647 (ends in 7)
            // INT_MIN = -2147483648 (ends in 8)
            if (result > Integer.MAX_VALUE / 10 || 
               (result == Integer.MAX_VALUE / 10 && digit > 7)) {
                return (sign == 1) ? Integer.MAX_VALUE : Integer.MIN_VALUE;
            }
            
            result = result * 10 + digit;
            i++;
        }
        
        return result * sign;
    }
}
