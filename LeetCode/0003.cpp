class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        std::set<char> current_chars;
        int longest_len = 0;
        int current_len = 0;
        auto start_it = s.begin();
        auto end_it = s.begin();
        while(end_it != s.end()) {
            if(start_it == end_it) {
                current_chars.insert(*end_it);
                end_it++;
                current_len++;
            } else if(current_chars.find(*end_it) == current_chars.end()) {
                current_chars.insert(*end_it);
                end_it++;
                current_len++;
            } else {
                current_chars.erase(*start_it);
                start_it++;
                current_len--;
            }
            if(current_len > longest_len) {
                longest_len = current_len;
            }
        }
        return(longest_len);
    }
};