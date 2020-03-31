class Solution {
public:
    int repeatedStringMatch(string A, string B) {
        string build_str = "";
        int num_concats = 0;
        while (build_str.length() < B.length()) {
            build_str.append(A);
            num_concats++;
        } 
        if (build_str.find(B) != std::string::npos) {
            return num_concats;
        }
        build_str.append(A);
        num_concats++;
        if (build_str.find(B) != std::string::npos) {
            return num_concats;
        } else {
            return -1;
        }
    }
};