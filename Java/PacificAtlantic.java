import java.util.ArrayList;
import java.util.List;

public class PacificAtlantic {
    public void flowsToBothOcean(int[][] heights, int rows, int cols, int i, int j, boolean[] oceanFlags) {
        // System.out.println("I: " + i + " ROWS: " + rows + " J: " + j + " COLS: " +
        // cols);
        if (i >= 0 && i <= rows && j >= 0 && j <= cols) {
            if ((j - 1) < 0)
                oceanFlags[0] = true;
            else if (heights[i][j - 1] < heights[i][j])
                flowsToBothOcean(heights, rows, cols, i, (j - 1), oceanFlags);

            if ((i - 1) < 0)
                oceanFlags[0] = true;
            else if (heights[i - 1][j] < heights[i][j])
                flowsToBothOcean(heights, rows, cols, (i - 1), j, oceanFlags);

            if ((j + 1) > cols)
                oceanFlags[1] = true;
            else if (heights[i][j + 1] < heights[i][j])
                flowsToBothOcean(heights, rows, cols, i, (j + 1), oceanFlags);

            if ((i + 1) > rows)
                oceanFlags[1] = true;
            else if (heights[i + 1][j] < heights[i][j])
                flowsToBothOcean(heights, rows, cols, (i + 1), j, oceanFlags);
        }
    }

    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        List<List<Integer>> results = new ArrayList<>();
        int numRows = heights.length;
        int numCols = heights[0].length;

        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j < numCols; j++) {
                boolean[] oceanFlags = new boolean[] { false, false };
                flowsToBothOcean(heights, (numRows - 1), (numCols - 1), i, j, oceanFlags);

                if (oceanFlags[0] && oceanFlags[1]) {
                    List<Integer> cell = new ArrayList<>();
                    cell.add(i);
                    cell.add(j);
                    results.add(cell);
                }
            }
        }

        return results;
    }

    public void func() {
        int[][] heights = new int[][] { { 1 } };
        // heights = new int[][] {
        // { 1, 2, 1 },
        // { 2, 1, 2 },
        // { 1, 2, 1 }
        // };
        System.out.println(pacificAtlantic(heights));
    }

    public static void main(String[] args) {
        PacificAtlantic obj = new PacificAtlantic();
        obj.func();
    }
}
