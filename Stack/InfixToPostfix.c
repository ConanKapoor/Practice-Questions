# include <stdio.h>
# include <stdlib.h>
# include <string.h>
# define bye return 0

char stack[100];
char postfix[100];
int head = -1;

char top(){
    if (head < 0){
        printf("Stack is empty. Add something to continue.");
    }
    else{
        return stack[head];
    }
}

void push(char value){
    if (head >= 100){
        printf("Stack is full. Pop something to push.");
    }
    else{
        stack[++head] = value;
    }
}

char pop(){

    if(head < 0){
        printf("Stack is empty. Add something to continue.");
    }
    else{
        char popped = stack[head];
        head--;
        return popped;
    }
}

void display(char* exp){
    int i;

    if(strlen(exp) == 0){
        printf("No postfix expression.");
    }
    else{
        printf("\tInfix expression: ");
        for (i=0; i<strlen(exp); i++){
            printf("%c", exp[i]);
        }
        printf("\n\tPostfix expression: ");
        for (i=0; i<strlen(exp); i++){
            printf("%c", postfix[i]);
        }
    }
}

int isOperand(char ch)
{
    return (ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z');
}

int Prec(char ch)
{
    switch (ch)
    {
    case '+':
    case '-':
        return 1;

    case '*':
    case '/':
        return 2;

    case '^':
        return 3;
    }
    return -1;
}

int infixToPrefix(char* exp){
    int i, j = -1, length = strlen(exp);

    for (i = 0; i < strlen(exp); i++){

        if (isOperand(exp[i])){
            postfix[++j] = exp[i];
        }
        else if (exp[i] == '('){
            push(exp[i]);
        }
        else if (exp[i] == ')')
        {
            while (head > -1 && top() != '(')
                postfix[++j] = pop();

            if (head > -1 && top() != '('){
                printf("Infix expression given is missing a paranthesis.");
                return -1;
            }
            else{
                pop()
            }
        }
        else{
            while (head > -1 && (Prec(exp[i])<=Prec(top()))){
                postfix[++j] = pop();

            push(exp[i]);
            }
        }
    }
    while (head != -1){
        postfix[++j] = pop();
    }
}

int main(){
    char exp[] = "a+b*(c^d-e)^(f+g*h)-i";
    infixToPrefix(exp);
    display(exp);
    bye;
}
