class Solution {
    public int search(int[] nums, int target) {
        int right = nums.length - 1;
        int left = 0;
        int middle = nums.length/2;
        while (right >= left){
            if (target == nums[middle]){
                return middle;
            }
            if (target > nums[middle]){
                left = middle + 1;
            }
            else {
                right = middle - 1;
            }
            middle = (right + left) / 2;
            
        }
        
        return -1;
    }
}
