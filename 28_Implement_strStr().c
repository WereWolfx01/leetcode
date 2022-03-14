

int strStr(char * haystack, char * needle){
    int lenA = strlen(haystack);
    int lenB = strlen(needle);
    
    if(lenA == 0 && lenB == 0){
        return 0;
    }
    
    for( int i = 0; i<lenA; i++ ){
        int j = 0;
        for(; j<lenB; j++){
            if(haystack[i + j] != needle[j]){
                break;
            }
        }
        if(j == lenB){
            return i;
        }
    }
    

    
    return -1;
    
}
