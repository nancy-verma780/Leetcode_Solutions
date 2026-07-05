bool isPalindrome(int x) {
    if (x < 0) {
        return false;
    }

    int num = x;
    int temp = x;
    long rev = 0;
    int digit;

    while (num > 0) {
        digit = num % 10;
        rev = (rev * 10) + digit;
        num /= 10;
    }

    return temp == rev;

}