class Solution {
public:
    int numberOfSteps (int num) {
        int num_steps = 0;
        if(num < 0) {
            return -1;
        }
        while (num > 0) {
            if (num%2 == 0) {
                num = num/2;
            } else {
                num--;
            }
            num_steps++;
        }
        return num_steps;
    }
};