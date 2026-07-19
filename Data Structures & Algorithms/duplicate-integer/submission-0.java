class Solution {
    public boolean hasDuplicate(int[] nums) {
        ArrayList<Integer> existing = new ArrayList<Integer>();
        for (int num : nums) {
            if (existing.contains(num)) {
                return true;
            } else {
                existing.add(num);
            }
        }
        return false;
    }
}