import java.lang.Math;

class Solution {
    public int arrangeCoins(int n) {
        return (int)((Math.sqrt(1 + 8 * (double)n) - 1) / 2.0);
    }
}