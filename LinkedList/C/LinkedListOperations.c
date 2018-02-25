# include <stdio.h>
# include <stdlib.h>
# include <stdbool.h>

struct node{
    int data;
    struct node *next;
};

void addNodeFront(struct node** head_ref, int value){

    struct node* new_node = (struct Node*) malloc (sizeof(struct node));

    new_node->data = value;
    new_node->next = (*head_ref);
    (*head_ref) = new_node;
}

void addAfter(struct node* prev_node, int value){
    if(prev_node == NULL){
        printf("Previous node can't be NULL. Sorry broda!");
    }

    struct node* new_node = (struct Node*) malloc (sizeof(struct node));

    new_node->data = value;
    new_node->next = prev_node->next;
    prev_node->next = new_node;
}

void addNodeEnd(struct node** head_ref, int value){

    struct node* new_node = (struct Node*) malloc (sizeof(struct node));
    struct node *last = *head_ref;

    new_node->data = value;
    new_node->next = NULL;

    if (*head_ref == NULL)
    {
       *head_ref = new_node;
       return;
    }

    while (last->next != NULL)
        last = last->next;

    last->next = new_node;
    return;
}

void deleteNode(struct node **head_ref, int value)
{

    struct node* temp = *head_ref, *prev;

    if (temp != NULL && temp->data == value)
    {
        *head_ref = temp->next;
        free(temp);
        return;
    }

    while (temp != NULL && temp->data != value)
    {
        prev = temp;
        temp = temp->next;
    }

    if (temp == NULL){
      return;
    }

    prev->next = temp->next;
    free(temp);
}

void deleteNodeAtPosition(struct node **head_ref, int position)
{
   if(*head_ref == NULL)
      return;

   struct node* temp = *head_ref;

    if(position == 0)
    {
        *head_ref = temp->next;
        free(temp);
        return;
    }

    for(int i=0; temp!=NULL && i<position-1; i++){
        temp = temp->next;
    }

    if(temp == NULL || temp->next == NULL){
        return;
    }

    struct Node *next = temp->next->next;
    free(temp->next);
    temp->next = next;
}

bool searchRecursive(struct node* head, int value)
{

    if (head == NULL){
        return false;
    }

    if (head->data == value){
        return true;
    }

    return searchRecursive(head->next, value);
}

bool searchIterative(struct node* head, int value)
{
    struct node* current = head;
    while (current != NULL)
    {
        if (current->data == value){
            return true;
        }
        current = current->next;
    }
    return false;
}

static void reverse(struct node** head_ref)
{
    struct node* prev   = NULL;
    struct node* current = *head_ref;
    struct node* next;
    while (current != NULL)
    {
        next  = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    *head_ref = prev;
}

void displayLL(struct node *node)
{
  while (node != NULL)
  {
     printf(" %d ", node->data);
     node = node->next;
  }
  printf("\n");
}

int main()
{
  struct node* head = NULL;

  addNodeEnd(&head, 6);
  displayLL(head);
  addNodeFront(&head, 7);
  displayLL(head);
  addNodeFront(&head, 1);
  displayLL(head);
  addNodeEnd(&head, 4);
  displayLL(head);
  addAfter(head->next, 8);

  printf("Created Linked list is: ");
  displayLL(head);

  return 0;
}
