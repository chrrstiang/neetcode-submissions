class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> uniqueNums = new HashSet<Integer>();

        if (nums.length == 0) {
            return 0;
        }

        for (int num : nums) {
            uniqueNums.add(num);
        }

        ArrayList<Integer> starts = new ArrayList<Integer>();

        for (int num : nums) {
            if(!uniqueNums.contains(num - 1)) {
                starts.add(num);
            }
        }

        int best = 1;
        ArrayList<Integer> curr = new ArrayList<Integer>();

        for (int num : starts) {
            curr.clear();
            curr.add(num);
            while (uniqueNums.contains(num + 1)) {
                curr.add(num + 1);
                if (curr.size() > best) {
                    best = curr.size();
                }
                num++;
            }
        }

        return best;
    }
}
