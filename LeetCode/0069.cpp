class Solution {
public:
    int mySqrt(int x) {
        //sanitize input before using log2
        if(x <= 0) {
            return 0;
        }
        //Make initial guess by right-shifting x by half its binary digit length
        double guess = 1.0 * (x >> static_cast<int>(log2(x)));
        //Use Newton's method for improving guess
        float error = 0.5;
        while ( abs(pow(guess, 2) - x) > error ) {
            guess = guess - (pow(guess, 2) - x) / (2 * guess);
        }
        return static_cast<int>(guess);
    }
};