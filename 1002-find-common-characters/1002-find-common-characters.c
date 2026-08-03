#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** commonChars(char** words, int wordsSize, int* returnSize) {
    // 1. Initialize global minimum frequencies with high values
    int min_freq[26];
    for (int i = 0; i < 26; i++) {
        min_freq[i] = 101; // Max word length constraint is 100
    }

    // 2. Count character frequencies for each word and update global minimums
    for (int i = 0; i < wordsSize; i++) {
        int current_freq[26] = {0};
        int len = strlen(words[i]);
        
        for (int j = 0; j < len; j++) {
            current_freq[words[i][j] - 'a']++;
        }
        
        for (int k = 0; k < 26; k++) {
            if (current_freq[k] < min_freq[k]) {
                min_freq[k] = current_freq[k];
            }
        }
    }

    // 3. Count total common characters to allocate exactly needed memory
    int total_chars = 0;
    for (int i = 0; i < 26; i++) {
        total_chars += min_freq[i];
    }

    // 4. Allocate memory for array of strings (each common char is a 2-byte string: char + '\0')
    char** result = (char**)malloc(total_chars * sizeof(char*));
    int index = 0;

    for (int i = 0; i < 26; i++) {
        while (min_freq[i] > 0) {
            result[index] = (char*)malloc(2 * sizeof(char));
            result[index][0] = i + 'a';
            result[index][1] = '\0';
            index++;
            min_freq[i]--;
        }
    }

    *returnSize = total_chars;
    return result;
}
