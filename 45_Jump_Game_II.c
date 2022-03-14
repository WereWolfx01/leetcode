int max(int a, int b){
    return (((a) > (b)) ? (a) : (b));
}

int jump(int* nums, int numsSize){
    int maxPos = 0;
    int end = 0;
    int depth = 0;
    
    for(int i=0; i<numsSize - 1; i++){
        maxPos = max(maxPos, i+nums[i]);
        
        if(i == end){
            end = maxPos;
            depth++;
        }
    }
    
    return depth;
}
