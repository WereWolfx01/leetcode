class Solution {
    public int[] searchRange(int[] nums, int target) {
        int[] result = {-1, -1};
        int left = binSearch(nums, target, true);
        int right = binSearch(nums, target, false);
        result[0] = left;
        result[1] = right;
        return result;
    }
    
    public int binSearch(int[] nums, int target, boolean leftBias){
        int left = 0, right = nums.length - 1;
        int index = -1;
        while (left <= right){
            int mid = (left + right) / 2;
            
            if (target > nums[mid]){
                left = mid  + 1;
            }
            else if (target < nums[mid]){
                right = mid - 1;
            }
            else{
                index = mid;
                if (leftBias){
                    right = mid - 1;
                }
                else{
                    left = mid + 1;
                }
            }
        }
        return index;
    }
}
