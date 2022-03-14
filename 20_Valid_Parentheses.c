

bool isValid(char * s){
    if(s == NULL){
        return true;
    }
    else if(strlen(s) == 0){
        return true;
    }
    int length = strlen(s);
    char *stack = (char *)malloc(length*sizeof(char));
    int i = 0;
    int top = -1;
    
    for(i = 0; i<length; i++){
        if(s[i] == '(' || s[i] == '{' || s[i] == '['){
            stack[++top] = s[i];
        }
        else{
            if(top == -1){
                return false;
            }
            else if(stack[top] == '(' && s[i] == ')'){
                top--;
            }
            else if(stack[top] == '{' && s[i] == '}'){
                top--;
            }
            else if(stack[top] == '[' && s[i] == ']'){
                top--;
            }
            else{
                return false;
            }
        }
    }
    if(top == -1){
        return true;
    }
    else{
        return false;
    }

}
