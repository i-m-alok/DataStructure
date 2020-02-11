#include<stdio.h>
struct node{
    int data;
    struct node *right;
    struct node *left;
};

int *insert(int data, struct node* root)
{
  if(root==NULL){
    struct node *temp;
    temp=(struct node*)malloc(sizeof(struct node));
    temp->data = data;
    temp->right=NULL;
    temp->left=NULL;
    root=&(temp[0]);
  }
  else{
      struct node *here;
      struct node *start;
      int rig;
      start = &(root[0]);
      here=&(root[0]);
      struct node *temp;
      temp=(struct node*)malloc(sizeof(struct node));
      temp->data = data;
      temp->right=NULL;
      temp->left=NULL;
    
      while(here!=NULL){
        if(data >= here->data){
          start=here;
          here=here->right;
          rig=1;
        }
        else{
          start=here;
          here=here->left;
          rig=0;
        }
      }
      if(rig==1){
        start->right=&(temp[0]);
        }
      else{
        start->left=&(temp[0]);
        }
  }
  return root;
}


int main(){
  int arr[6]={5,6,3,1,8,7};
  struct node* ptr=NULL;
  for(int i=0; i<6; i++){
    ptr=insert(arr[i], ptr);
  }
}