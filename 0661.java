class Solution {
    public int[][] imageSmoother(int[][] M) {
        if(M.length == 0) {
            return new int[][]{};
        }
        int height = M.length;
        int width = M[0].length;
        int[][] result = new int[height][width];
        int average = 0;
        List<Integer[]> neighbors;
        for(int y = 0; y < height; y++) {
            for(int x = 0; x < width; x++, average = 0) {
                neighbors = findNeighbors(x, y, width, height);
                for(Integer[] neighbor: neighbors) {
                    average += M[neighbor[1]][neighbor[0]];
                }
                average = average / neighbors.size();
                result[y][x] = average;
            }
        }
        return result;
        
    }
    private List<Integer[]> findNeighbors(int x, int y, int width, int height) {
        List<Integer[]> result = new ArrayList<>();
        for(int i = -1; i < 2; i++){
            for(int j = -1; j < 2; j++) {
                int newX = x + i;
                int newY = y + j;
                if(newX >= 0 && newX < width && newY >= 0 && newY < height) {
                    result.add(new Integer[]{newX, newY});
                }
            }
        }
        return result;
    }
}