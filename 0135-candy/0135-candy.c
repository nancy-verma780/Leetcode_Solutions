int candy(int* ratings, int ratingsSize) {
    if (ratingsSize <= 1) {
        return ratingsSize;
    }

    int total_candies = 1;
    int up = 0;
    int down = 0;
    int peak = 0;

    for (int i = 1; i < ratingsSize; i++) {
        if (ratings[i] > ratings[i - 1]) {
            up++;
            down = 0;
            peak = up;
            total_candies += 1 + up;
        } 
        else if (ratings[i] == ratings[i - 1]) {
            up = 0;
            down = 0;
            peak = 0;
            total_candies += 1;
        } 
        else {
            down++;
            up = 0;
            total_candies += down;
            if (down > peak) {
                total_candies += 1;
            }
        }
    }

    return total_candies;
}