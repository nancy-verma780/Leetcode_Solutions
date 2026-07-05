/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
char ***ans;
int *colSizes;
int ansSize;

void solve(int row, int n, int cols, int diag1, int diag2,
           char **board)
{
    if (row == n)
    {
        ans[ansSize] = (char **)malloc(n * sizeof(char *));
        colSizes[ansSize] = n;

        for (int i = 0; i < n; i++)
        {
            ans[ansSize][i] = (char *)malloc((n + 1) * sizeof(char));
            strcpy(ans[ansSize][i], board[i]);
        }

        ansSize++;
        return;
    }

    int available = ((1 << n) - 1) & ~(cols | diag1 | diag2);

    while (available)
    {
        int pos = available & (-available);
        available -= pos;

        int col = 0;
        int temp = pos;
        while (temp > 1)
        {
            temp >>= 1;
            col++;
        }

        board[row][col] = 'Q';

        solve(row + 1,
              n,
              cols | pos,
              (diag1 | pos) << 1,
              (diag2 | pos) >> 1,
              board);

        board[row][col] = '.';
    }
}

char ***solveNQueens(int n, int *returnSize, int **returnColumnSizes)
{
    ans = (char ***)malloc(400 * sizeof(char **));
    colSizes = (int *)malloc(400 * sizeof(int));
    ansSize = 0;

    char **board = (char **)malloc(n * sizeof(char *));
    for (int i = 0; i < n; i++)
    {
        board[i] = (char *)malloc((n + 1) * sizeof(char));
        memset(board[i], '.', n);
        board[i][n] = '\0';
    }

    solve(0, n, 0, 0, 0, board);

    *returnSize = ansSize;
    *returnColumnSizes = colSizes;

    for (int i = 0; i < n; i++)
        free(board[i]);
    free(board);

    return ans;
}