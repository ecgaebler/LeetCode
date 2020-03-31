/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    int getDecimalValue(ListNode* head) {
        int result = 0;
        ListNode* current_node = head;
        while(current_node != NULL) {
            result = (2 * result) + current_node->val;
            current_node = current_node->next;
        }
        return result;
    }
};