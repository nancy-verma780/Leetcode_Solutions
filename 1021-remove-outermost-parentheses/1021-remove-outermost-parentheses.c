char* removeOuterParentheses(char* s) {
    int len = strlen(s);
    char* result = (char*)malloc((len + 1) * sizeof(char));
    int opened = 0;
    int index = 0;

    for (int i = 0; i < len; i++) {
        if (s[i] == '(') {
            if (opened > 0) {
                result[index++] = s[i];
            }
            opened++;
        } else {
            opened--;
            if (opened > 0) {
                result[index++] = s[i];
            }
        }
    }
    result[index] = '\0';
    return result;
}
