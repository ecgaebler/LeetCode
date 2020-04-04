class Solution {
public:
    bool isHappy(int n) {
        set<int> visited;
        int new_value;
        while (n != 1) {
            new_value = 0;
            while (n > 0) {
                new_value += pow((n % 10), 2);
                n = n / 10;
            }
            if (!visited.insert(new_value).second) {
                return false;
            }
            n = new_value;
        }
        return true;
    }
};