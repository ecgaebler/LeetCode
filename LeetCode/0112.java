/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
import java.util.*;

class Solution {
    public boolean hasPathSum(TreeNode root, int sum) {
        if(root == null) {
            return false;
        }
        Deque<Pair<TreeNode, Integer>> stack = new ArrayDeque<Pair<TreeNode, Integer>>();
        stack.push(new Pair<TreeNode, Integer>(root, sum));
        while(stack.size() > 0) {
            Pair<TreeNode, Integer> nodeAndSum = stack.pop();
            TreeNode node = nodeAndSum.getKey();
            int targetSum = nodeAndSum.getValue() - node.val;
            if(node.left == null && node.right == null && targetSum == 0) {
                return true;
            }
            if(node.left != null) {
                stack.push(new Pair<TreeNode, Integer>(node.left, targetSum));
            }
            if(node.right != null) {
                stack.push(new Pair<TreeNode, Integer>(node.right, targetSum));
            }
        }
        return(false);
    }
}