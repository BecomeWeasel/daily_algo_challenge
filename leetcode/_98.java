

class _98 {

    private class TreeNode {

        int val;
        TreeNode left;
        TreeNode right;

        TreeNode() {
        }

        TreeNode(int val) {
            this.val = val;
        }

        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }


    public boolean isValidBST(TreeNode root) {
        return isValid(root.left, null, root.val) && isValid(root.right, root.val, null);
    }

    // 왼쪽 자식은 max 값을 가지고 있고
    // 오른쪽 자식은 min 값을 가지고 있음
    private boolean isValid(TreeNode root, Integer min, Integer max) {

        // 존재하지 않는 자식에 대한 호출이였으니 검증 필요 X
        if (root == null) {
            return true;
        }

        if (min == null && max != null && root.val>=max) return false;

        if (min != null && max == null && root.val<=min) return false;

        if (min != null && max != null) {
            if (!(root.val > min && root.val < max)) {
                return false;
            }
        }
        // 내가 왼쪽 자식이면 m=null , M!=null
        // 내 왼쪽 서브트리는 -inf < val < root.val
        // 내 오른쪽 서브트리는 root.val < val < max

        // 내가 오른쪽 자식이면 m!=null M=null
        // 내 왼쪽 서브트리는 min < val < root.val
        // 내 오른쪽 서브트리는 root.val < val < inf

        // 둘다 제한이 걸려있으면
        // 내 왼쪽 서브트리는 min < val < root.val
        // 내 오른쪽 서브트리는 root.val < val < max

        return isValid(root.left, min, root.val) && isValid(root.right, root.val, max);
    }


}