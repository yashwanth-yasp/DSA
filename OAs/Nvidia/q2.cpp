
#include <iostream>
#include <bits/stdc++.h>

using namespace std;


struct node{
    int value;
    struct node * next;
};

void reorder(struct node * list){
    struct node * a, * b;
    int temp;

    if (!list || !list->next) return;

    a = list;
    b = list->next;
    while(b){
        temp = a->value;
        a->value = b->value;
        b->value = temp;
        a = b->next;
        b = a ? a->next : 0;
    }

    cout << "Reordered list: ";
    while(list){
        cout << list->value << " ";
        list = list->next;
    }
}

int main(){
    // list = 1->3->2->4->7->6->9
    struct node * list = new node;
    list->value = 1;
    list->next = new node;
    list->next->value = 3;
    list->next->next = new node;
    list->next->next->value = 2;
    list->next->next->next = new node;
    list->next->next->next->value = 4;
    list->next->next->next->next = new node;
    list->next->next->next->next->value = 7;
    list->next->next->next->next->next = new node;
    list->next->next->next->next->next->value = 6;
    list->next->next->next->next->next->next = new node;
    list->next->next->next->next->next->next->value = 9;
    list->next->next->next->next->next->next->next = 0;
    
    reorder(list);
}