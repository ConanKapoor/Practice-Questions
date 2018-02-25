# include <stdio.h>
# include <stdlib.h>
# define bye return 0

int stack[100],head=-1;

void top(){
    if (head < 0){
        printf("Stack is empty. Add something to continue.");
    }
    else{
        printf("\tThe value at top is: %d\n",stack[head]);
    }
}

void push(int value){
    if (head >= 100){
        printf("Stack is full. Pop something to push.");
    }
    else{
        head++;
        stack[head] = value;
    }
}

void pop(){
    if(head < 0){
        printf("Stack is empty. Add something to continue.");
    }
    else{
        head--;
    }
}

void display(){
    int i;

    if(head < 0){
        printf("Stack is empty. Add something to continue.");
    }
    else{
        printf("\tValues in stack are:");
        for (i=0; i<=head; i++){
            printf(" %d", stack[i]);
        }
    }
}

int main(){
    push(1);
    push(2);
    push(3);
    pop();
    push(4);
    top();
    display();
    bye;
}
