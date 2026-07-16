int lengthOfLongestSubstring(char *s) {
    int lastIndex[128];

    // Initialize all indices to -1
    for (int i = 0; i < 128; i++) {
        lastIndex[i] = -1;
    }

    int left = 0;
    int maxLength = 0;

    for (int right = 0; s[right] != '\0'; right++) {
        // If character is repeated inside current window
        if (lastIndex[s[right]] >= left) {
            left = lastIndex[s[right]] + 1;
        }

        // Update last seen index
        lastIndex[s[right]] = right;

        // Update maximum length
        int currentLength = right - left + 1;
        if (currentLength > maxLength) {
            maxLength = currentLength;
        }
    }

    return maxLength;
}