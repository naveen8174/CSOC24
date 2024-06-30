#include<stdio.h>
//sorting in python is out of contxt as it's so simple.
void bubble_sort(int a[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n-i-1; j++) {
            if (a[j] > a[j+1]) {
                int tmp = a[j];
                a[j] = a[j+1];
                a[j+1] = tmp;
            }
        }
    }
}
void insertion(int a[],int n){
    for(int i=1;i<n;i++){
        int key=a[i];
        int j=i-1;
        
        while (j>=0 && a[j] > key) {
            a[j+1]=a[j];
            j=j-1;
        }
        a[j+1]=key;
    }
}
int main(){
    int array[]={23,17,45,8,11,56,67};
    bubble_sort(array,7);
    for (int i=0;i<7;i++){
        printf("%d ",array[i]);
    }
    
}