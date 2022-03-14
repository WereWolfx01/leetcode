

int removeDuplicates(int* nums, int numsSize){
    int i, j;
    
    j = 1;
    for(i=1; i<numsSize; i++){
        if( nums[i-1] < nums[i] ){
            printf("%d %d ", nums[i-1], nums[i] );
            nums[j] = nums[i];
            j++;
        }
    }
    return j;
}
