class Solution {
    public int[] productExceptSelf(int[] nums) {
        int total = 1;
        int[] before = new int[nums.length];
        int[] after = new int[nums.length];

        for (int i = 0; i < nums.length; i++) {
            if (i == 0) {
                before[i] = 1;
            } else {
                before[i] = before[i - 1] * nums[i - 1];
            }
        }

        for (int i = nums.length - 1; i >= 0; i--) {
            if (i == nums.length - 1) {
                after[i] = 1;
            } else {
                after[i] = after[i + 1] * nums[i + 1];
            }
        }

        int[] res = new int[nums.length];

        for (int i = 0; i < nums.length; i++) {
            res[i] = before[i] * after[i];
        }
        
        return res;
    }
}  
