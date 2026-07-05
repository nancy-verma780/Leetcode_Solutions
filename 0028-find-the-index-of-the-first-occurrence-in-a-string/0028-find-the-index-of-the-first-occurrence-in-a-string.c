int strStr(char *haystack, char *needle) {
    if (*needle == '\0')
        return 0;

    int m = strlen(needle);
    int *lps = (int *)malloc(m * sizeof(int));

    lps[0] = 0;
    int len = 0;

    for (int i = 1; i < m;) {
        if (needle[i] == needle[len]) {
            lps[i++] = ++len;
        } else if (len) {
            len = lps[len - 1];
        } else {
            lps[i++] = 0;
        }
    }

    int i = 0, j = 0;

    while (haystack[i]) {
        if (haystack[i] == needle[j]) {
            i++;
            j++;

            if (j == m) {
                free(lps);
                return i - j;
            }
        } else if (j) {
            j = lps[j - 1];
        } else {
            i++;
        }
    }

    free(lps);
    return -1;
}